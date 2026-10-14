from django.db import models

from concepts.models import Concept


class PYQ(models.Model):
    academy = models.ForeignKey(
        "academies.Academy",
        on_delete=models.CASCADE,
        related_name="pyqs",
    )
    year = models.PositiveIntegerField()
    question = models.TextField()
    answer_key = models.TextField(blank=True, default="")
    concepts = models.ManyToManyField(Concept, related_name="pyqs", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-year", "id"]
        verbose_name = "PYQ"
        verbose_name_plural = "PYQs"

    def __str__(self):
        return f"[{self.year}] {self.question[:60]}"
