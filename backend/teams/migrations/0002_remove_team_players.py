# Generated by Django 4.1.2 on 2022-10-22 01:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("teams", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="team", name="players",),
    ]
