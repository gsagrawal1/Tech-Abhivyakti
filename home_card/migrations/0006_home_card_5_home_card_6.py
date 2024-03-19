# Generated by Django 5.0.1 on 2024-03-19 12:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home_card", "0005_remove_home_card_1_card_author_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="home_card_5",
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
                (
                    "card_desc",
                    models.CharField(default=None, max_length=250, null=True),
                ),
                (
                    "card_image",
                    models.ImageField(
                        default=None, max_length=250, null=True, upload_to="homecard1/"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="home_card_6",
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
                (
                    "card_desc",
                    models.CharField(default=None, max_length=250, null=True),
                ),
                (
                    "card_image",
                    models.ImageField(
                        default=None, max_length=250, null=True, upload_to="homecard1/"
                    ),
                ),
            ],
        ),
    ]