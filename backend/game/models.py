from django.db import models
from django.db.models import JSONField


class Game(models.Model):
    ball_by_ball = models.CharField(max_length=300)
    league_type = models.CharField(max_length=1)

    def __str__(self):
        return f'Game #{self.id}: {self.league_type}'


class ARCLGame(models.Model):
    league_type = models.CharField(max_length=1)
    batsmen = JSONField()
    bowlers = JSONField()
    data = JSONField()

    def __str__(self):
        return f'ARCL Game #{self.id}: {self.league_type}'
