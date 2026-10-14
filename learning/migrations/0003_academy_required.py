from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("academies", "0002_backfill_fortuneias"),
        (
            "learning",
            "0002_alter_userconceptprogress_unique_together_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="userconceptprogress",
            name="academy",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="concept_progress",
                to="academies.academy",
            ),
        ),
    ]
