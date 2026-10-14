from django.db import models
from django.utils.text import slugify

from subjects.models import Chapter, Subject


class Concept(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        PUBLISHED = "published", "Published"

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="concepts",
    )
    chapter = models.ForeignKey(
        Chapter,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="concepts",
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=280)
    summary = models.TextField(blank=True, default="")
    body = models.TextField(
        blank=True,
        default="",
        help_text="Markdown explanation shown on the concept page.",
    )
    visual_blocks = models.JSONField(
        default=list,
        blank=True,
        help_text=(
            "Ordered visual blocks — see docs/VISUAL_GRAMMARS.md "
            "(mental_model, pillars, tree, timeline, flowchart, journey, "
            "comparison, pyq_heatmap, article_explorer, case_network, "
            "memory_palace, simulator, relation_graph, map, callout, markdown)."
        ),
    )
    sort_order = models.PositiveSmallIntegerField(
        default=0,
        help_text="Order within the chapter.",
        db_index=True,
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PUBLISHED,
        db_index=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["sort_order", "title"]
        unique_together = [("subject", "slug")]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:280]
        super().save(*args, **kwargs)


class ConceptEdge(models.Model):
    class RelationType(models.TextChoices):
        PARENT = "parent", "Parent"
        RELATED = "related", "Related"
        PREREQUISITE = "prerequisite", "Prerequisite"

    source = models.ForeignKey(
        Concept,
        on_delete=models.CASCADE,
        related_name="outgoing_edges",
    )
    target = models.ForeignKey(
        Concept,
        on_delete=models.CASCADE,
        related_name="incoming_edges",
    )
    relation_type = models.CharField(
        max_length=32,
        choices=RelationType.choices,
        default=RelationType.RELATED,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["relation_type", "id"]
        unique_together = [("source", "target", "relation_type")]

    def __str__(self):
        return f"{self.source} —{self.relation_type}→ {self.target}"


class ConceptArticle(models.Model):
    concept = models.ForeignKey(
        Concept,
        on_delete=models.CASCADE,
        related_name="articles",
    )
    ref = models.CharField(max_length=120, help_text="e.g. Article 110")
    excerpt = models.TextField(blank=True, default="")
    sort_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["sort_order", "id"]

    def __str__(self):
        return f"{self.ref} ({self.concept})"


class CaseLaw(models.Model):
    class Court(models.TextChoices):
        SC = "sc", "Supreme Court"
        HC = "hc", "High Court"
        OTHER = "other", "Other"

    academy = models.ForeignKey(
        "academies.Academy",
        on_delete=models.CASCADE,
        related_name="case_laws",
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=280)
    parties = models.CharField(max_length=255, blank=True, default="")
    year = models.PositiveIntegerField()
    court = models.CharField(
        max_length=16,
        choices=Court.choices,
        default=Court.SC,
    )
    summary = models.TextField(blank=True, default="")
    holding = models.TextField(
        blank=True,
        default="",
        help_text="Short holding / ratio for revision.",
    )
    concepts = models.ManyToManyField(
        Concept,
        related_name="case_laws",
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-year", "title"]
        verbose_name = "Case law"
        verbose_name_plural = "Case laws"
        unique_together = [("academy", "slug")]

    def __str__(self):
        return f"{self.title} ({self.year})"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:280]
        super().save(*args, **kwargs)


class ConstitutionalAmendment(models.Model):
    academy = models.ForeignKey(
        "academies.Academy",
        on_delete=models.CASCADE,
        related_name="amendments",
    )
    number = models.PositiveIntegerField(
        help_text="Amendment number, e.g. 44 for the 44th Amendment.",
    )
    year = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    summary = models.TextField(blank=True, default="")
    effect = models.TextField(
        blank=True,
        default="",
        help_text="Short constitutional effect for revision.",
    )
    concepts = models.ManyToManyField(
        Concept,
        related_name="amendments",
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["number"]
        verbose_name = "Constitutional amendment"
        verbose_name_plural = "Constitutional amendments"
        unique_together = [("academy", "number")]

    def __str__(self):
        return f"{self.number}th Amendment ({self.year})"
