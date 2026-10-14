# Generated manually for FR visual MVP

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("concepts", "0001_initial"),
        ("subjects", "0002_chapter"),
    ]

    operations = [
        migrations.AddField(
            model_name="concept",
            name="chapter",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="concepts",
                to="subjects.chapter",
            ),
        ),
        migrations.AddField(
            model_name="concept",
            name="sort_order",
            field=models.PositiveSmallIntegerField(
                db_index=True,
                default=0,
                help_text="Order within the chapter.",
            ),
        ),
        migrations.AddField(
            model_name="concept",
            name="visual_blocks",
            field=models.JSONField(
                blank=True,
                default=list,
                help_text="Ordered visual blocks: map, flowchart, comparison, callout, markdown.",
            ),
        ),
        migrations.AlterModelOptions(
            name="concept",
            options={"ordering": ["sort_order", "title"]},
        ),
    ]
