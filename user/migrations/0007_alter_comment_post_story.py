# Generated by Django 5.0.1 on 2024-03-18 10:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0006_remove_post_comments_comment"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="stories",
                to="user.post",
            ),
        ),
        migrations.CreateModel(
            name="Story",
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
                ("contenttext", models.TextField(blank=True, default=None, null=True)),
                (
                    "contentbackground",
                    models.TextField(blank=True, default=None, null=True),
                ),
                (
                    "contentfstyle",
                    models.TextField(blank=True, default=None, null=True),
                ),
                (
                    "storyfile",
                    models.FileField(
                        blank=True,
                        default=None,
                        max_length=500,
                        null=True,
                        upload_to="posts/",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
