from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("academies", "0002_backfill_fortuneias"),
        (
            "concepts",
            "0005_alter_constitutionalamendment_unique_together_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="caselaw",
            name="academy",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="case_laws",
                to="academies.academy",
            ),
        ),
        migrations.AlterField(
            model_name="constitutionalamendment",
            name="academy",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="amendments",
                to="academies.academy",
            ),
        ),
    ]
