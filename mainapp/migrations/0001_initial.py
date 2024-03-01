# Generated by Django 5.0.2 on 2024-03-01 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Attendee",
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
                ("firstname", models.CharField(max_length=50)),
                ("lastname", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("company_name", models.CharField(max_length=50)),
                ("country", models.CharField(max_length=50)),
                ("phone_number", models.CharField(max_length=50)),
                ("gender", models.CharField(max_length=50)),
            ],
        ),
    ]