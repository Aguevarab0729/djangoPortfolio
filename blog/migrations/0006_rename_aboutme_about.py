# Generated by Django 4.1.7 on 2023-02-18 11:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0005_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="AboutMe",
            new_name="About",
        ),
    ]
