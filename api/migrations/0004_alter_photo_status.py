# Generated by Django 5.0.3 on 2024-03-14 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_comment_author_comment_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photo",
            name="status",
            field=models.CharField(
                choices=[
                    ("App", "Approved"),
                    ("Rej", "Rejected"),
                    ("Del", "Deleted"),
                    ("Mod", "Moderation"),
                ],
                default="Mod",
                max_length=3,
            ),
        ),
    ]
