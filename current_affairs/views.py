import calendar
import hashlib
import random
from datetime import date

from django.db.models import Count, Q
from django.utils import timezone
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from academies.models import Academy
from academies.permissions import IsAcademyStaffOrSuperuser
from academies.utils import require_academy

from .models import CADocument, CAQuestion, QuizAttempt
from .serializers import (
    CADocumentSerializer,
    CAQuestionPublicSerializer,
    QuizAttemptDetailSerializer,
    QuizAttemptListSerializer,
    QuizStartSerializer,
    QuizSubmitSerializer,
    StaffCADocumentReplaceSerializer,
    StaffCADocumentSerializer,
    StaffCADocumentUploadSerializer,
    StaffCAQuestionSerializer,
    StaffFinderSyncSerializer,
    ordered_questions,
)
from .services.analytics import academy_analytics, student_analytics
from .services.attempt_answers import replace_answer_rows


def _month_bounds(d: date) -> tuple[date, date]:
    first = d.replace(day=1)
    last_day = calendar.monthrange(d.year, d.month)[1]
    return first, date(d.year, d.month, last_day)


def _published_qs(academy: Academy):
    return CAQuestion.objects.filter(
        is_published=True,
        document__status=CADocument.Status.READY,
        document__academy=academy,
    ).select_related("document")


def _apply_subject_tags(qs, subject_tags: list[str] | None):
    if subject_tags:
        return qs.filter(subject_tag__in=subject_tags)
    return qs


def _pick_for_daily(
    academy: Academy,
    d: date,
    subject_tags: list[str] | None = None,
) -> tuple[list[CAQuestion], date, date]:
    doc = (
        CADocument.objects.filter(
            academy=academy,
            doc_type=CADocument.DocType.DAILY,
            source_date=d,
            status=CADocument.Status.READY,
        )
        .order_by("-id")
        .first()
    )
    if not doc:
        return [], d, d
    qs = list(
        _apply_subject_tags(_published_qs(academy).filter(document=doc), subject_tags)
        .order_by("sort_order", "id")
    )
    return qs, doc.period_start, doc.period_end


def _pick_for_monthly(
    academy: Academy,
    d: date,
    subject_tags: list[str] | None = None,
) -> tuple[list[CAQuestion], date, date]:
    start, end = _month_bounds(d)
    doc = (
        CADocument.objects.filter(
            academy=academy,
            doc_type=CADocument.DocType.MONTHLY,
            source_date=start,
            status=CADocument.Status.READY,
        )
        .order_by("-id")
        .first()
    )
    if not doc:
        return [], start, end
    qs = list(
        _apply_subject_tags(_published_qs(academy).filter(document=doc), subject_tags)
        .order_by("sort_order", "id")
    )
    return qs, doc.period_start, doc.period_end


def _pick_for_range(
    academy: Academy,
    start: date,
    end: date,
    limit: int | None,
    seed: str,
    subject_tags: list[str] | None = None,
) -> list[CAQuestion]:
    # Dailies: any day overlapping the range.
    # Monthlies: only when the range fully covers that month's period.
    qs = list(
        _apply_subject_tags(
            _published_qs(academy).filter(
                Q(
                    document__doc_type=CADocument.DocType.DAILY,
                    document__period_end__gte=start,
                    document__period_start__lte=end,
                )
                | Q(
                    document__doc_type=CADocument.DocType.MONTHLY,
                    document__period_start__gte=start,
                    document__period_end__lte=end,
                )
            ),
            subject_tags,
        ).order_by("document__period_start", "sort_order", "id")
    )
    if limit is None or len(qs) <= limit:
        return qs
    rng = random.Random(int(hashlib.sha256(seed.encode()).hexdigest()[:8], 16))
    return rng.sample(qs, limit)


class DocumentListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = CADocumentSerializer
    pagination_class = None

    def get_queryset(self):
        academy = require_academy(self.request)
        qs = CADocument.objects.filter(
            academy=academy,
            status=CADocument.Status.READY,
        ).annotate(
            published_question_count=Count(
                "questions",
                filter=Q(questions__is_published=True),
            )
        )
        doc_type = self.request.query_params.get("doc_type")
        if doc_type in {CADocument.DocType.DAILY, CADocument.DocType.MONTHLY}:
            qs = qs.filter(doc_type=doc_type)
        return qs


class QuizStartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        academy = require_academy(request)
        serializer = QuizStartSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        mode = data["mode"]
        limit = data.get("limit")
        subject_tags = data.get("subject_tags")

        if mode == QuizAttempt.Mode.DAILY:
            questions, p_start, p_end = _pick_for_daily(
                academy, data["date"], subject_tags
            )
        elif mode == QuizAttempt.Mode.MONTHLY:
            questions, p_start, p_end = _pick_for_monthly(
                academy, data["date"], subject_tags
            )
        else:
            p_start, p_end = data["start"], data["end"]
            seed = f"{request.user.id}:{p_start}:{p_end}:{timezone.now().isoformat()}"
            questions = _pick_for_range(
                academy, p_start, p_end, limit, seed, subject_tags
            )

        if not questions:
            return Response(
                {
                    "detail": "No published questions available for that selection."
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        if mode != QuizAttempt.Mode.RANGE and limit is not None:
            questions = questions[:limit]

        attempt = QuizAttempt.objects.create(
            academy=academy,
            user=request.user,
            mode=mode,
            period_start=p_start,
            period_end=p_end,
            question_ids=[q.id for q in questions],
            total=len(questions),
        )
        return Response(
            {
                "id": attempt.id,
                "mode": attempt.mode,
                "period_start": attempt.period_start,
                "period_end": attempt.period_end,
                "total": attempt.total,
                "questions": CAQuestionPublicSerializer(
                    questions, many=True
                ).data,
            },
            status=status.HTTP_201_CREATED,
        )


class QuizDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        academy = require_academy(request)
        try:
            attempt = QuizAttempt.objects.get(
                pk=pk, user=request.user, academy=academy
            )
        except QuizAttempt.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(QuizAttemptDetailSerializer(attempt).data)


class QuizSubmitView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        academy = require_academy(request)
        try:
            attempt = QuizAttempt.objects.get(
                pk=pk, user=request.user, academy=academy
            )
        except QuizAttempt.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if attempt.is_completed:
            return Response(
                QuizAttemptDetailSerializer(attempt).data,
                status=status.HTTP_200_OK,
            )

        serializer = QuizSubmitSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        raw_answers = serializer.validated_data["answers"]
        answers = {str(k): v for k, v in raw_answers.items()}

        score = 0
        for q in ordered_questions(attempt.question_ids):
            if answers.get(str(q.id)) == q.correct_option:
                score += 1

        attempt.answers = answers
        attempt.score = score
        attempt.total = len(attempt.question_ids)
        attempt.completed_at = timezone.now()
        attempt.save(
            update_fields=[
                "answers",
                "score",
                "total",
                "completed_at",
                "updated_at",
            ]
        )
        replace_answer_rows(attempt, answers=answers)
        return Response(QuizAttemptDetailSerializer(attempt).data)


class AttemptListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = QuizAttemptListSerializer
    pagination_class = None

    def get_queryset(self):
        academy = require_academy(self.request)
        return QuizAttempt.objects.filter(
            user=self.request.user, academy=academy
        )


def _parse_days(request) -> int:
    raw = request.query_params.get("days", "90")
    try:
        return int(raw)
    except (TypeError, ValueError):
        return 90


class MyAnalyticsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        academy = require_academy(request)
        return Response(
            student_analytics(
                academy, request.user.id, days=_parse_days(request)
            )
        )


class AcademyAnalyticsView(APIView):
    permission_classes = [IsAuthenticated, IsAcademyStaffOrSuperuser]

    def get(self, request):
        academy = require_academy(request)
        return Response(academy_analytics(academy, days=_parse_days(request)))


class AcademyStudentAnalyticsView(APIView):
    permission_classes = [IsAuthenticated, IsAcademyStaffOrSuperuser]

    def get(self, request, user_id: int):
        academy = require_academy(request)
        from django.contrib.auth import get_user_model

        User = get_user_model()
        if not User.objects.filter(pk=user_id).exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(
            student_analytics(academy, user_id, days=_parse_days(request))
        )


def _staff_document_qs(academy: Academy):
    return CADocument.objects.filter(academy=academy).annotate(
        question_count=Count("questions"),
        published_question_count=Count(
            "questions",
            filter=Q(questions__is_published=True),
        ),
    )


class StaffDocumentListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsAcademyStaffOrSuperuser]
    pagination_class = None

    def get_serializer_class(self):
        if self.request.method == "POST":
            return StaffCADocumentUploadSerializer
        return StaffCADocumentSerializer

    def get_queryset(self):
        academy = require_academy(self.request)
        qs = _staff_document_qs(academy)
        doc_type = self.request.query_params.get("doc_type")
        if doc_type in {CADocument.DocType.DAILY, CADocument.DocType.MONTHLY}:
            qs = qs.filter(doc_type=doc_type)
        return qs

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx["academy"] = require_academy(self.request)
        return ctx

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        doc = serializer.save()
        doc = _staff_document_qs(doc.academy).get(pk=doc.pk)
        return Response(
            StaffCADocumentSerializer(doc).data,
            status=status.HTTP_201_CREATED,
        )


class StaffDocumentDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsAcademyStaffOrSuperuser]
    http_method_names = ["get", "patch", "delete", "head", "options"]

    def get_queryset(self):
        academy = require_academy(self.request)
        return _staff_document_qs(academy)

    def get_serializer_class(self):
        if self.request.method == "PATCH":
            return StaffCADocumentReplaceSerializer
        return StaffCADocumentSerializer

    def _reject_if_processing(self, doc: CADocument):
        if doc.status == CADocument.Status.PROCESSING:
            return Response(
                {
                    "detail": (
                        "Document is currently generating. "
                        "Try again when finished."
                    )
                },
                status=status.HTTP_409_CONFLICT,
            )
        return None

    def partial_update(self, request, *args, **kwargs):
        doc = self.get_object()
        blocked = self._reject_if_processing(doc)
        if blocked is not None:
            return blocked
        serializer = self.get_serializer(doc, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        doc = _staff_document_qs(require_academy(request)).get(pk=doc.pk)
        return Response(StaffCADocumentSerializer(doc).data)

    def destroy(self, request, *args, **kwargs):
        doc = self.get_object()
        blocked = self._reject_if_processing(doc)
        if blocked is not None:
            return blocked
        if doc.file:
            doc.file.delete(save=False)
        doc.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StaffDocumentRegenerateView(APIView):
    permission_classes = [IsAuthenticated, IsAcademyStaffOrSuperuser]

    def post(self, request, pk):
        academy = require_academy(request)
        try:
            doc = CADocument.objects.get(pk=pk, academy=academy)
        except CADocument.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if doc.status == CADocument.Status.PROCESSING:
            return Response(
                {
                    "detail": (
                        "Document is currently generating. "
                        "Try again when finished."
                    )
                },
                status=status.HTTP_409_CONFLICT,
            )

        from .signals import _enqueue

        CADocument.objects.filter(pk=doc.pk).update(
            status=CADocument.Status.PENDING,
            error_message="",
        )
        _enqueue(doc.pk, force=True)
        doc = _staff_document_qs(academy).get(pk=doc.pk)
        return Response(StaffCADocumentSerializer(doc).data)


class StaffFinderSyncView(APIView):
    """Enqueue scrape + ingest + generation for a daily FINDER date range."""

    permission_classes = [IsAuthenticated, IsAcademyStaffOrSuperuser]

    def post(self, request):
        academy = require_academy(request)
        serializer = StaffFinderSyncSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        start = serializer.validated_data["start"]
        end = serializer.validated_data["end"]
        regenerate = serializer.validated_data["regenerate"]

        processing = CADocument.objects.filter(
            academy=academy,
            doc_type=CADocument.DocType.DAILY,
            source_date__gte=start,
            source_date__lte=end,
            status=CADocument.Status.PROCESSING,
        ).exists()
        if processing:
            return Response(
                {
                    "detail": (
                        "One or more documents in this range are currently "
                        "generating. Try again when finished."
                    )
                },
                status=status.HTTP_409_CONFLICT,
            )

        from .tasks import sync_finder_range

        async_result = sync_finder_range.apply_async(
            args=[academy.pk, start.isoformat(), end.isoformat()],
            kwargs={"regenerate": regenerate},
            ignore_result=False,
        )
        mode = "fill + regenerate" if regenerate else "fill gaps"
        return Response(
            {
                "task_id": async_result.id,
                "start": start.isoformat(),
                "end": end.isoformat(),
                "regenerate": regenerate,
                "message": (
                    f"FINDER sync queued ({mode}) for "
                    f"{start.isoformat()} → {end.isoformat()}. "
                    "Documents will move to pending/processing as they run."
                ),
            },
            status=status.HTTP_202_ACCEPTED,
        )


class StaffDocumentQuestionsView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsAcademyStaffOrSuperuser]
    serializer_class = StaffCAQuestionSerializer
    pagination_class = None

    def get_queryset(self):
        academy = require_academy(self.request)
        return CAQuestion.objects.filter(
            document_id=self.kwargs["pk"],
            document__academy=academy,
        ).order_by("sort_order", "id")


class StaffQuestionPatchView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsAcademyStaffOrSuperuser]
    serializer_class = StaffCAQuestionSerializer
    http_method_names = ["patch", "head", "options"]

    def get_queryset(self):
        academy = require_academy(self.request)
        return CAQuestion.objects.filter(document__academy=academy)
