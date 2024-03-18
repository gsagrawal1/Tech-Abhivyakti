# Generated by Django 5.0.1 on 2024-03-17 12:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0004_alter_post_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.FileField(
                blank=True, default=None, max_length=500, null=True, upload_to="posts/"
            ),
        ),
    ]
