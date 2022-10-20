# Generated by Django 4.1.2 on 2022-10-20 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Game",
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
                ("ball_by_ball", models.CharField(max_length=300)),
                ("league_type", models.IntegerField()),
            ],
        ),
    ]
