# Generated by Django 5.0.1 on 2024-03-17 12:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0002_post_comments_post_image_alter_post_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="comments",
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="content",
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.FileField(blank=True, default=None, null=True, upload_to=""),
        ),
    ]
