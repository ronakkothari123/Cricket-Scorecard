from django.db import models
from enum import Enum


class LeagueTypes(Enum):
    ARCL = 0
    OTHER = 1


class Game(models.Model):
    ball_by_ball = models.CharField(max_length=300)
    league_type = models.IntegerField()

    def __str__(self):
        return f'Game: {self.league_type}'
