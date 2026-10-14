from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("academies", "0002_backfill_fortuneias"),
        ("questions", "0002_pyq_academy"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pyq",
            name="academy",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pyqs",
                to="academies.academy",
            ),
        ),
    ]
