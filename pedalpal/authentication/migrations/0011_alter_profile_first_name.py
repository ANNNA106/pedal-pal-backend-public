# Generated by Django 4.2.10 on 2024-02-25 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0010_alter_profile_first_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="first_name",
            field=models.CharField(default="", max_length=50, null=True),
        ),
    ]
