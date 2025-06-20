# Generated by Django 5.2.3 on 2025-06-16 13:23

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ChaiVarity",
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
                ("name", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="chai/varity/")),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "chai_type",
                    models.CharField(
                        choices=[
                            ("ML", "MASALA"),
                            ("GR", "GINGER"),
                            ("EL", "ELAICHI"),
                            ("PL", "PALNE"),
                            ("KL", "KIWI"),
                        ],
                        max_length=2,
                    ),
                ),
            ],
        ),
    ]
