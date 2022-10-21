from rest_framework import serializers
from .models import Game


class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ('ball_by_ball', 'league_type', 'batsmen', 'bowlers', 'extra_data')

