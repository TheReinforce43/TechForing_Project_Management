# Generated by Django 4.2.7 on 2024-12-27 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Project", "0005_projectmodel_owner_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="projectmodel",
            name="project_end_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
