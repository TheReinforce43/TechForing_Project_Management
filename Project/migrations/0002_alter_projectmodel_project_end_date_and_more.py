# Generated by Django 4.2.7 on 2024-12-19 12:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("Project", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="projectmodel",
            name="project_end_date",
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="projectmodel",
            name="project_start_date",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
