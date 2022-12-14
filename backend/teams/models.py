from django.db import models


# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=50, default=None, null=True)
    league_type = models.CharField(max_length=1, default="N")
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    no_result = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name} ({self.league_type}): {self.wins}-{self.losses}-{self.draws}'
