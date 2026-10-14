from django.db import migrations

from academies.models import generate_invite_code

FORTUNEIAS_SLUG = "fortuneias"
FORTUNEIAS_NAME = "Fortune IAS"


def backfill_fortuneias(apps, schema_editor):
    Academy = apps.get_model("academies", "Academy")
    academy, _ = Academy.objects.get_or_create(
        slug=FORTUNEIAS_SLUG,
        defaults={
            "name": FORTUNEIAS_NAME,
            "display_name": FORTUNEIAS_NAME,
            "invite_code": generate_invite_code(),
            "is_active": True,
        },
    )

    for app_label, model_name in (
        ("subjects", "Subject"),
        ("concepts", "CaseLaw"),
        ("concepts", "ConstitutionalAmendment"),
        ("questions", "PYQ"),
        ("current_affairs", "CADocument"),
        ("current_affairs", "QuizAttempt"),
        ("learning", "UserConceptProgress"),
    ):
        Model = apps.get_model(app_label, model_name)
        Model.objects.filter(academy__isnull=True).update(academy=academy)


def noop_reverse(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ("academies", "0001_initial"),
        ("subjects", "0003_subject_academy_alter_subject_slug_and_more"),
        (
            "concepts",
            "0005_alter_constitutionalamendment_unique_together_and_more",
        ),
        ("questions", "0002_pyq_academy"),
        (
            "current_affairs",
            "0002_remove_cadocument_uniq_ca_document_type_date_and_more",
        ),
        (
            "learning",
            "0002_alter_userconceptprogress_unique_together_and_more",
        ),
    ]

    operations = [
        migrations.RunPython(backfill_fortuneias, noop_reverse),
    ]
