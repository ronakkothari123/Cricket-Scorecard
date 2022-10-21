from django.db import models
from django.db.models import JSONField
from users.models import Profile


class Game(models.Model):
    ball_by_ball = models.CharField(max_length=300)
    league_type = models.CharField(max_length=1)
    batsmen = JSONField(default=None, null=True)
    bowlers = JSONField(default=None, null=True)
    extra_data = JSONField(default=None, null=True)

    creator = models.ForeignKey(Profile, on_delete=models.CASCADE, default=None, null=True)


def __str__(self):
    return f'Game #{self.id}: {self.league_type}'
