# Generated by Django 4.2.10 on 2024-03-06 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0004_remove_booking_status_booking_cancelled"),
    ]

    operations = [
        migrations.AddField(
            model_name="lock",
            name="arduino_port",
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
