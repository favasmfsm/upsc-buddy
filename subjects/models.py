from django.db import models
from django.utils.text import slugify


class Subject(models.Model):
    academy = models.ForeignKey(
        "academies.Academy",
        on_delete=models.CASCADE,
        related_name="subjects",
    )
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140)
    description = models.TextField(blank=True, default="")
    sort_order = models.PositiveSmallIntegerField(
        default=0,
        help_text="Browse order for the subject catalog.",
        db_index=True,
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["sort_order", "name"]
        unique_together = [("academy", "slug")]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)[:140]
        super().save(*args, **kwargs)


class Section(models.Model):
    """Broader part / book division under a subject (e.g. Laxmikanth Part I)."""

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="sections",
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=280)
    sort_order = models.PositiveSmallIntegerField(
        default=0,
        help_text="Part / browse order within the subject.",
        db_index=True,
    )
    summary = models.TextField(blank=True, default="")
    is_published = models.BooleanField(default=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["sort_order", "title"]
        unique_together = [("subject", "slug")]

    def __str__(self):
        return f"Part {self.sort_order}. {self.title}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:280]
        super().save(*args, **kwargs)


class Chapter(models.Model):
    """Syllabus-branch / browse spine for concepts under a subject."""

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="chapters",
    )
    section = models.ForeignKey(
        Section,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="chapters",
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=280)
    sort_order = models.PositiveSmallIntegerField(
        default=0,
        help_text="Syllabus branch / browse order.",
        db_index=True,
    )
    book_ref = models.CharField(
        max_length=255,
        blank=True,
        default="",
        help_text='e.g. "Laxmikanth 8th Ed, Ch. 8"',
    )
    summary = models.TextField(blank=True, default="")
    is_published = models.BooleanField(default=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["sort_order", "title"]
        unique_together = [("subject", "slug")]

    def __str__(self):
        return f"{self.sort_order}. {self.title}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:280]
        super().save(*args, **kwargs)
