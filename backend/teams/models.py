from django.db import models
from users.models import Profile


# Create your models here.
class Team(models.Model):
    players = models.ManyToManyField(Profile, default=None, null=True)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    no_result = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.wins}-{self.losses}-{self.draws}'
