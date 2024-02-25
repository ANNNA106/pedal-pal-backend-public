# Generated by Django 4.2.10 on 2024-02-24 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("analytics", "0003_statistics_user"),
        ("booking", "0001_initial"),
        ("auth", "0012_alter_user_first_name_max_length"),
        ("maintenance", "0002_alter_feedback_user"),
        ("admin", "0003_logentry_add_action_flag_choices"),
        ("authtoken", "0003_tokenproxy"),
        ("authentication", "0003_delete_profile_customuser_groups_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="CustomUser",
            new_name="Profile",
        ),
    ]
