from django.conf import settings
from django.db import models
from django.utils import timezone

from concepts.models import Concept


class UserConceptProgress(models.Model):
    class Status(models.TextChoices):
        NOT_STARTED = "not_started", "Not started"
        STUDIED = "studied", "Studied"
        REVISE_LATER = "revise_later", "Revise later"

    academy = models.ForeignKey(
        "academies.Academy",
        on_delete=models.CASCADE,
        related_name="concept_progress",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="concept_progress",
    )
    concept = models.ForeignKey(
        Concept,
        on_delete=models.CASCADE,
        related_name="user_progress",
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NOT_STARTED,
        db_index=True,
    )
    is_difficult = models.BooleanField(default=False, db_index=True)
    last_studied_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-updated_at"]
        unique_together = [("user", "academy", "concept")]
        verbose_name_plural = "user concept progress"

    def __str__(self):
        return f"{self.user} — {self.concept} ({self.status})"

    def mark(self, status: str):
        self.status = status
        if status == self.Status.STUDIED:
            self.last_studied_at = timezone.now()
        self.save()

    def set_difficult(self, is_difficult: bool):
        self.is_difficult = is_difficult
        self.save(update_fields=["is_difficult", "updated_at"])
