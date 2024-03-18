# Generated by Django 5.0.1 on 2024-03-17 11:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="comments",
            field=models.TextField(default=None, null=True),
        ),
        migrations.AddField(
            model_name="post",
            name="image",
            field=models.FileField(default=None, null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="post",
            name="content",
            field=models.TextField(default=None, null=True),
        ),
    ]
