from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("academies", "0002_backfill_fortuneias"),
        ("subjects", "0003_subject_academy_alter_subject_slug_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subject",
            name="academy",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="subjects",
                to="academies.academy",
            ),
        ),
    ]
