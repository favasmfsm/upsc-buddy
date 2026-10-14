# Generated manually for FR visual MVP

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("subjects", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Chapter",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("slug", models.SlugField(max_length=280)),
                (
                    "sort_order",
                    models.PositiveSmallIntegerField(
                        db_index=True,
                        default=0,
                        help_text="Laxmikanth chapter number / browse order.",
                    ),
                ),
                (
                    "book_ref",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text='e.g. "Laxmikanth 8th Ed, Ch. 8"',
                        max_length=255,
                    ),
                ),
                ("summary", models.TextField(blank=True, default="")),
                (
                    "is_published",
                    models.BooleanField(db_index=True, default=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="chapters",
                        to="subjects.subject",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order", "title"],
                "unique_together": {("subject", "slug")},
            },
        ),
    ]
