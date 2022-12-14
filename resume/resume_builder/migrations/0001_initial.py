# Generated by Django 4.1 on 2022-10-18 17:20

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Resume",
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
                ("firstname", models.CharField(max_length=255)),
                ("lastname", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=255, unique=True)),
                ("phone", models.CharField(max_length=255, unique=True)),
                ("country", models.CharField(blank=True, max_length=255)),
                ("city", models.CharField(blank=True, max_length=255)),
                ("desired_position", models.CharField(max_length=255)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("professional_summary", models.TextField(blank=True, null=True)),
                (
                    "user_img",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
                ("references", models.TextField(blank=True, null=True)),
                ("career_obj", models.TextField(blank=True, null=True)),
                ("education", models.TextField(blank=True, null=True)),
                ("job_1_description", models.TextField(blank=True, null=True)),
                ("job_1_start_dt", models.DateTimeField(blank=True, null=True)),
                ("job_1_end_dt", models.DateTimeField(blank=True, null=True)),
                ("job_2_description", models.TextField(blank=True, null=True)),
                ("job_2_start_dt", models.DateTimeField(blank=True, null=True)),
                ("job_2_end_dt", models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
