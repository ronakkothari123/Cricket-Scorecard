from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    runs = models.IntegerField(default=0)
    balls = models.IntegerField(default=0)
    matches = models.IntegerField(default=0)
    innings = models.IntegerField(default=0)
    batting_innings = models.IntegerField(default=0)
    bowling_innings = models.IntegerField(default=0)
    wickets = models.IntegerField(default=0)
    overs = models.IntegerField(default=0)
    bowling_runs = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username}: {self.runs} ({self.balls})'
