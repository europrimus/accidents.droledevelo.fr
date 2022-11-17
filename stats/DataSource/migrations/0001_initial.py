# Generated by Django 4.1.3 on 2022-11-17 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="URL",
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
                ("uid", models.CharField(max_length=36, unique=True)),
                ("title", models.CharField(max_length=150)),
                ("description", models.CharField(max_length=500, null=True)),
                ("url", models.CharField(max_length=250)),
                (
                    "checksum_type",
                    models.CharField(
                        choices=[("sha1", "sha1")], max_length=4, null=True
                    ),
                ),
                ("checksum_value", models.CharField(max_length=50, null=True)),
                ("filesize", models.PositiveIntegerField(null=True)),
                (
                    "mime_type",
                    models.CharField(
                        choices=[
                            ("text/csv", "csv"),
                            ("application/pdf", "pdf"),
                            ("application/json", "json"),
                        ],
                        max_length=16,
                        null=True,
                    ),
                ),
                ("created_at", models.DateTimeField(null=True)),
                ("published_at", models.DateTimeField(null=True)),
                ("last_modified_at", models.DateTimeField(null=True)),
                ("imported_at", models.DateTimeField(null=True)),
            ],
        ),
    ]