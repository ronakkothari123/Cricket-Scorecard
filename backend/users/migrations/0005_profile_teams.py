# Generated by Django 4.1.2 on 2022-10-22 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("teams", "0002_remove_team_players"),
        ("users", "0004_profile_pfp_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="teams",
            field=models.ManyToManyField(default=None, null=True, to="teams.team"),
        ),
    ]
