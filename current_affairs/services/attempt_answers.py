"""Helpers for persisting normalized quiz attempt answer rows."""

from __future__ import annotations

from ..models import CAQuestion, QuizAttempt, QuizAttemptAnswer
from ..serializers import ordered_questions
from ..subjects import normalize_subject_tag


def build_answer_rows(
    attempt: QuizAttempt,
    answers: dict[str, str] | None = None,
) -> list[QuizAttemptAnswer]:
    """
    Build QuizAttemptAnswer instances for an attempt (not saved).

    `answers` defaults to attempt.answers JSON ({qid: "A"|"B"|...}).
    Missing keys count as skipped (empty selected_option, is_correct=False).
    """
    payload = answers if answers is not None else (attempt.answers or {})
    rows: list[QuizAttemptAnswer] = []
    for q in ordered_questions(attempt.question_ids):
        selected = str(payload.get(str(q.id)) or "").strip().upper()
        if selected not in {"A", "B", "C", "D"}:
            selected = ""
        rows.append(
            QuizAttemptAnswer(
                attempt=attempt,
                question=q,
                selected_option=selected,
                is_correct=bool(selected) and selected == q.correct_option,
                subject_tag=normalize_subject_tag(q.subject_tag),
                source_topic=(q.source_topic or "").strip()[:255],
            )
        )
    return rows


def replace_answer_rows(
    attempt: QuizAttempt,
    answers: dict[str, str] | None = None,
) -> int:
    """Delete existing rows and bulk_create fresh ones. Returns count created."""
    rows = build_answer_rows(attempt, answers=answers)
    QuizAttemptAnswer.objects.filter(attempt=attempt).delete()
    if rows:
        QuizAttemptAnswer.objects.bulk_create(rows)
    return len(rows)


def normalize_question_subject_tags(*, batch_size: int = 500) -> int:
    """Rewrite CAQuestion.subject_tag onto the allowlist. Returns rows updated."""
    updated = 0
    qs = CAQuestion.objects.all().only("id", "subject_tag")
    batch: list[CAQuestion] = []
    for question in qs.iterator(chunk_size=batch_size):
        canonical = normalize_subject_tag(question.subject_tag)
        if canonical != question.subject_tag:
            question.subject_tag = canonical
            batch.append(question)
        if len(batch) >= batch_size:
            CAQuestion.objects.bulk_update(batch, ["subject_tag"])
            updated += len(batch)
            batch = []
    if batch:
        CAQuestion.objects.bulk_update(batch, ["subject_tag"])
        updated += len(batch)
    return updated
