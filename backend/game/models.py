from django.db import models


class Game(models.Model):
    LEAGUE_CHOICES = (
        ('A', 'ARCL'),
        ('O', 'Other')
    )

    ball_by_ball = models.CharField(max_length=300)
    league_type = models.CharField(max_length=1, choices=LEAGUE_CHOICES)

    def __str__(self):
        return f'Game: {self.league_type}'
