# Generated by Django 5.0.1 on 2024-02-14 17:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home_card", "0003_home_card_2_home_card_3_home_card_4"),
    ]

    operations = [
        migrations.AddField(
            model_name="home_card_1",
            name="card_lng",
            field=models.CharField(default=None, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="home_card_2",
            name="card_lng",
            field=models.CharField(default=None, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="home_card_3",
            name="card_lng",
            field=models.CharField(default=None, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="home_card_4",
            name="card_lng",
            field=models.CharField(default=None, max_length=30, null=True),
        ),
    ]
