from django.db import models


class Game(models.Model):
    ball_by_ball = models.CharField(max_length=300)
    league_type = models.CharField(max_length=1)

    def __str__(self):
        return f'Game: {self.league_type}'
