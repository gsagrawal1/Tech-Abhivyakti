# Generated by Django 5.0.1 on 2024-03-19 13:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home_card", "0007_book_card_1_book_card_2_book_card_3_book_card_4_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="sport_card_1",
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
            name="sport_card_2",
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
            name="sport_card_3",
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
            name="sport_card_4",
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
            name="sport_card_5",
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
