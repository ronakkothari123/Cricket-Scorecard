# Generated by Django 4.1.2 on 2022-10-22 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("teams", "0002_remove_team_players"),
    ]

    operations = [
        migrations.AddField(
            model_name="team",
            name="league_type",
            field=models.CharField(default="N", max_length=1),
        ),
        migrations.AddField(
            model_name="team",
            name="name",
            field=models.CharField(default=None, max_length=50, null=True),
        ),
    ]