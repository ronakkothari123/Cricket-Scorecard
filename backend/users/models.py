from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    runs = models.IntegerField()
    matches = models.IntegerField()
    innings = models.IntegerField()
    batting_innings = models.IntegerField()
    bowling_innings = models.IntegerField()
    wickets = models.IntegerField()
    overs = models.IntegerField()
    bowling_runs = models.IntegerField()

