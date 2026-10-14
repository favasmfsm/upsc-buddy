"""Aggregation helpers for Current Affairs quiz analytics."""

from __future__ import annotations

from datetime import timedelta
from typing import Any

from django.db.models import Avg, Count, F, FloatField, Max, Q
from django.db.models.functions import Cast, Coalesce
from django.utils import timezone

from academies.models import Academy

from ..models import QuizAttempt, QuizAttemptAnswer


def _pct(correct: int, total: int) -> float | None:
    if total <= 0:
        return None
    return round(100.0 * correct / total, 1)


def _days_cutoff(days: int):
    days = max(1, min(int(days or 90), 3650))
    return timezone.now() - timedelta(days=days), days


def _completed_attempts_qs(academy: Academy, *, user_id: int | None, since):
    qs = QuizAttempt.objects.filter(
        academy=academy,
        completed_at__isnull=False,
        completed_at__gte=since,
    )
    if user_id is not None:
        qs = qs.filter(user_id=user_id)
    return qs


def _answer_qs(academy: Academy, *, user_id: int | None, since):
    qs = QuizAttemptAnswer.objects.filter(
        attempt__academy=academy,
        attempt__completed_at__isnull=False,
        attempt__completed_at__gte=since,
    )
    if user_id is not None:
        qs = qs.filter(attempt__user_id=user_id)
    return qs


def _by_subject(answer_qs) -> list[dict[str, Any]]:
    rows = (
        answer_qs.values("subject_tag")
        .annotate(
            total=Count("id"),
            correct=Count("id", filter=Q(is_correct=True)),
        )
        .order_by("subject_tag")
    )
    return [
        {
            "subject_tag": r["subject_tag"] or "Other",
            "correct": r["correct"],
            "total": r["total"],
            "accuracy_pct": _pct(r["correct"], r["total"]),
        }
        for r in rows
    ]


def _weak_topics(
    answer_qs, *, limit: int = 10, min_total: int = 3
) -> list[dict[str, Any]]:
    rows = (
        answer_qs.exclude(source_topic="")
        .values("source_topic", "subject_tag")
        .annotate(
            total=Count("id"),
            correct=Count("id", filter=Q(is_correct=True)),
        )
        .filter(total__gte=min_total)
    )
    enriched = [
        {
            "source_topic": r["source_topic"],
            "subject_tag": r["subject_tag"] or "Other",
            "correct": r["correct"],
            "total": r["total"],
            "accuracy_pct": _pct(r["correct"], r["total"]),
        }
        for r in rows
    ]
    enriched.sort(
        key=lambda r: (
            r["accuracy_pct"] if r["accuracy_pct"] is not None else 101,
            -r["total"],
        )
    )
    return enriched[:limit]


def _score_series(attempts_qs) -> list[dict[str, Any]]:
    series = []
    for a in attempts_qs.order_by("completed_at").only(
        "id", "completed_at", "score", "total", "mode"
    ):
        total = a.total or 0
        score = a.score if a.score is not None else 0
        series.append(
            {
                "attempt_id": a.id,
                "completed_at": a.completed_at.isoformat() if a.completed_at else None,
                "score": score,
                "total": total,
                "accuracy_pct": _pct(score, total),
                "mode": a.mode,
            }
        )
    return series


def student_analytics(
    academy: Academy,
    user_id: int,
    *,
    days: int = 90,
) -> dict[str, Any]:
    since, days = _days_cutoff(days)
    attempts_qs = _completed_attempts_qs(academy, user_id=user_id, since=since)
    answer_qs = _answer_qs(academy, user_id=user_id, since=since)

    attempt_count = attempts_qs.count()
    answer_agg = answer_qs.aggregate(
        questions_answered=Count("id"),
        correct=Count("id", filter=Q(is_correct=True)),
    )
    questions_answered = answer_agg["questions_answered"] or 0
    correct = answer_agg["correct"] or 0

    # Average of per-attempt score percentages (avoid div-by-zero via Coalesce)
    avg_score = attempts_qs.annotate(
        score_pct=Cast(Coalesce(F("score"), 0), FloatField())
        * 100.0
        / Cast(Coalesce(F("total"), 1), FloatField())
    ).aggregate(avg=Avg("score_pct"))["avg"]

    return {
        "days": days,
        "summary": {
            "attempts": attempt_count,
            "questions_answered": questions_answered,
            "accuracy_pct": _pct(correct, questions_answered),
            "avg_score_pct": round(avg_score, 1) if avg_score is not None else None,
        },
        "score_series": _score_series(attempts_qs),
        "by_subject": _by_subject(answer_qs),
        "weak_topics": _weak_topics(answer_qs),
    }


def academy_analytics(academy: Academy, *, days: int = 90) -> dict[str, Any]:
    since, days = _days_cutoff(days)
    attempts_qs = _completed_attempts_qs(academy, user_id=None, since=since)
    answer_qs = _answer_qs(academy, user_id=None, since=since)

    active_students = attempts_qs.values("user_id").distinct().count()
    total_attempts = attempts_qs.count()
    answer_agg = answer_qs.aggregate(
        questions=Count("id"),
        correct=Count("id", filter=Q(is_correct=True)),
    )
    questions = answer_agg["questions"] or 0
    correct = answer_agg["correct"] or 0

    per_user = answer_qs.values("attempt__user_id", "attempt__user__email").annotate(
        questions=Count("id"),
        correct=Count("id", filter=Q(is_correct=True)),
        attempts=Count("attempt_id", distinct=True),
        last_attempt_at=Max("attempt__completed_at"),
    )
    attempt_meta = {
        r["user_id"]: r
        for r in attempts_qs.values("user_id", "user__email").annotate(
            attempts=Count("id"),
            last_attempt_at=Max("completed_at"),
        )
    }

    students: list[dict[str, Any]] = []
    seen: set[int] = set()
    for r in per_user:
        uid = r["attempt__user_id"]
        seen.add(uid)
        students.append(
            {
                "user_id": uid,
                "email": r["attempt__user__email"],
                "attempts": r["attempts"],
                "accuracy_pct": _pct(r["correct"], r["questions"]),
                "last_attempt_at": (
                    r["last_attempt_at"].isoformat() if r["last_attempt_at"] else None
                ),
            }
        )

    for uid, meta in attempt_meta.items():
        if uid in seen:
            continue
        students.append(
            {
                "user_id": uid,
                "email": meta["user__email"],
                "attempts": meta["attempts"],
                "accuracy_pct": None,
                "last_attempt_at": (
                    meta["last_attempt_at"].isoformat()
                    if meta["last_attempt_at"]
                    else None
                ),
            }
        )

    students.sort(
        key=lambda s: (
            s["accuracy_pct"] is None,
            s["accuracy_pct"] if s["accuracy_pct"] is not None else 101,
            -(s["attempts"] or 0),
        )
    )

    return {
        "days": days,
        "summary": {
            "active_students": active_students,
            "total_attempts": total_attempts,
            "avg_accuracy_pct": _pct(correct, questions),
        },
        "by_subject": _by_subject(answer_qs),
        "students": students,
    }
