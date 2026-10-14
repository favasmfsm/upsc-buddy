import calendar
from datetime import date

from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.db import models


def ca_document_upload_to(instance, filename):
    kind = instance.doc_type or "misc"
    return f"current_affairs/{kind}/{filename}"


class CADocument(models.Model):
    class DocType(models.TextChoices):
        DAILY = "daily", "Daily"
        MONTHLY = "monthly", "Monthly"

    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        PROCESSING = "processing", "Processing"
        READY = "ready", "Ready"
        FAILED = "failed", "Failed"

    academy = models.ForeignKey(
        "academies.Academy",
        on_delete=models.CASCADE,
        related_name="ca_documents",
    )
    doc_type = models.CharField(max_length=16, choices=DocType.choices, db_index=True)
    title = models.CharField(max_length=255)
    source_date = models.DateField(
        help_text="Calendar date for daily; first of month for monthly.",
        db_index=True,
    )
    period_start = models.DateField(db_index=True)
    period_end = models.DateField(db_index=True)
    file = models.FileField(
        upload_to=ca_document_upload_to,
        validators=[FileExtensionValidator(["pdf"])],
    )
    status = models.CharField(
        max_length=16,
        choices=Status.choices,
        default=Status.PENDING,
        db_index=True,
    )
    error_message = models.TextField(blank=True, default="")
    gemini_model = models.CharField(max_length=64, blank=True, default="")
    generated_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-source_date", "-id"]
        constraints = [
            models.UniqueConstraint(
                fields=["academy", "doc_type", "source_date"],
                name="uniq_ca_document_academy_type_date",
            )
        ]
        verbose_name = "CA document"
        verbose_name_plural = "CA documents"

    def __str__(self):
        return f"{self.get_doc_type_display()} — {self.title} ({self.source_date})"

    def fill_period_bounds(self):
        if self.doc_type == self.DocType.DAILY:
            self.period_start = self.source_date
            self.period_end = self.source_date
        elif self.doc_type == self.DocType.MONTHLY:
            self.source_date = self.source_date.replace(day=1)
            last_day = calendar.monthrange(
                self.source_date.year, self.source_date.month
            )[1]
            self.period_start = self.source_date
            self.period_end = date(
                self.source_date.year, self.source_date.month, last_day
            )

    def save(self, *args, **kwargs):
        if self.source_date:
            self.fill_period_bounds()
        super().save(*args, **kwargs)

class CAQuestion(models.Model):
    class CorrectOption(models.TextChoices):
        A = "A", "A"
        B = "B", "B"
        C = "C", "C"
        D = "D", "D"

    document = models.ForeignKey(
        CADocument,
        on_delete=models.CASCADE,
        related_name="questions",
    )
    stem = models.TextField()
    option_a = models.TextField()
    option_b = models.TextField()
    option_c = models.TextField()
    option_d = models.TextField()
    correct_option = models.CharField(max_length=1, choices=CorrectOption.choices)
    explanation = models.TextField(blank=True, default="")
    subject_tag = models.CharField(max_length=64, blank=True, default="")
    source_topic = models.CharField(max_length=255, blank=True, default="")
    is_published = models.BooleanField(default=True, db_index=True)
    sort_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["document_id", "sort_order", "id"]
        verbose_name = "CA question"
        verbose_name_plural = "CA questions"

    def __str__(self):
        return self.stem[:80]


class QuizAttempt(models.Model):
    class Mode(models.TextChoices):
        DAILY = "daily", "Daily"
        MONTHLY = "monthly", "Monthly"
        RANGE = "range", "Date range"

    academy = models.ForeignKey(
        "academies.Academy",
        on_delete=models.CASCADE,
        related_name="quiz_attempts",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="ca_quiz_attempts",
    )
    mode = models.CharField(max_length=16, choices=Mode.choices, db_index=True)
    period_start = models.DateField()
    period_end = models.DateField()
    question_ids = models.JSONField(default=list)
    answers = models.JSONField(default=dict, blank=True)
    score = models.PositiveIntegerField(null=True, blank=True)
    total = models.PositiveIntegerField(default=0)
    completed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Quiz attempt"
        verbose_name_plural = "Quiz attempts"

    def __str__(self):
        return f"{self.user} {self.mode} {self.period_start}→{self.period_end}"

    @property
    def is_completed(self):
        return self.completed_at is not None


class QuizAttemptAnswer(models.Model):
    """Per-question row for a completed (or backfilled) quiz attempt."""

    attempt = models.ForeignKey(
        QuizAttempt,
        on_delete=models.CASCADE,
        related_name="answer_rows",
    )
    question = models.ForeignKey(
        CAQuestion,
        on_delete=models.CASCADE,
        related_name="attempt_answers",
    )
    selected_option = models.CharField(max_length=1, blank=True, default="")
    is_correct = models.BooleanField(default=False, db_index=True)
    subject_tag = models.CharField(max_length=64, blank=True, default="", db_index=True)
    source_topic = models.CharField(max_length=255, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["attempt_id", "id"]
        constraints = [
            models.UniqueConstraint(
                fields=["attempt", "question"],
                name="uniq_ca_attempt_answer_attempt_question",
            )
        ]
        indexes = [
            models.Index(
                fields=["subject_tag", "is_correct"],
                name="ca_answer_subject_correct_idx",
            ),
        ]
        verbose_name = "Quiz attempt answer"
        verbose_name_plural = "Quiz attempt answers"

    def __str__(self):
        return f"attempt={self.attempt_id} q={self.question_id} correct={self.is_correct}"
