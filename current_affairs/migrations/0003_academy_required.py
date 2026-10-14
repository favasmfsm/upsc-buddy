from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("academies", "0002_backfill_fortuneias"),
        (
            "current_affairs",
            "0002_remove_cadocument_uniq_ca_document_type_date_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="cadocument",
            name="academy",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ca_documents",
                to="academies.academy",
            ),
        ),
        migrations.AlterField(
            model_name="quizattempt",
            name="academy",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="quiz_attempts",
                to="academies.academy",
            ),
        ),
    ]
