# Generated by Django 4.1.2 on 2022-10-21 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("game", "0003_arclgame"),
    ]

    operations = [
        migrations.RenameModel(old_name="ARCLGame", new_name="ARCL",),
        migrations.RenameField(
            model_name="arcl", old_name="data", new_name="extra_data",
        ),
    ]
