# Generated by Django 4.1.2 on 2022-10-21 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_batting_innings_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='balls',
            field=models.IntegerField(default=0),
        ),
    ]
