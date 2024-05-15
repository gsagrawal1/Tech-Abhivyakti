# Generated by Django 5.0.1 on 2024-03-22 12:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0012_rename_eventaddress_events_eventaddressp_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="events",
            old_name="eventfr_till",
            new_name="eventfr_tillday",
        ),
        migrations.AddField(
            model_name="events",
            name="eventfr_tillmonth",
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name="events",
            name="eventfr_tillyear",
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]