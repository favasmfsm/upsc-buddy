import secrets
import string

from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.text import slugify

from .storage import branding_storage


def generate_invite_code(length: int = 10) -> str:
    alphabet = string.ascii_uppercase + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(length))


def academy_logo_upload_to(instance, filename):
    return f"academies/logos/{instance.slug}/{filename}"


def academy_favicon_upload_to(instance, filename):
    return f"academies/favicons/{instance.slug}/{filename}"


class Academy(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=80, unique=True)
    display_name = models.CharField(
        max_length=120,
        blank=True,
        default="",
        help_text="Branding name shown in the UI. Defaults to name.",
    )
    tagline = models.CharField(max_length=200, blank=True, default="")
    invite_code = models.CharField(max_length=32, unique=True, db_index=True)
    logo_url = models.URLField(
        blank=True,
        default="",
        help_text="Legacy external logo URL. Prefer uploading logo.",
    )
    logo = models.ImageField(
        upload_to=academy_logo_upload_to,
        storage=branding_storage,
        blank=True,
        null=True,
        validators=[FileExtensionValidator(["png", "jpg", "jpeg", "webp", "gif"])],
    )
    favicon = models.FileField(
        upload_to=academy_favicon_upload_to,
        storage=branding_storage,
        blank=True,
        null=True,
        validators=[FileExtensionValidator(["ico", "png", "svg", "webp"])],
    )
    primary_color = models.CharField(
        max_length=32,
        blank=True,
        default="",
        help_text="Optional CSS color, e.g. #1a4d3e",
    )
    is_active = models.BooleanField(default=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "academies"

    def __str__(self):
        return self.display_name or self.name

    @property
    def branding_name(self) -> str:
        return self.display_name or self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)[:80]
        if not self.display_name:
            self.display_name = self.name
        if not self.invite_code:
            self.invite_code = generate_invite_code()
        super().save(*args, **kwargs)

    def rotate_invite_code(self) -> str:
        self.invite_code = generate_invite_code()
        self.save(update_fields=["invite_code", "updated_at"])
        return self.invite_code


class AcademyMembership(models.Model):
    class Role(models.TextChoices):
        ADMIN = "admin", "Admin"
        STAFF = "staff", "Staff"
        STUDENT = "student", "Student"

    academy = models.ForeignKey(
        Academy,
        on_delete=models.CASCADE,
        related_name="memberships",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="academy_memberships",
    )
    role = models.CharField(
        max_length=16,
        choices=Role.choices,
        default=Role.STUDENT,
        db_index=True,
    )
    is_active = models.BooleanField(default=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["academy__name", "user__email"]
        unique_together = [("academy", "user")]

    def __str__(self):
        return f"{self.user} @ {self.academy} ({self.role})"
