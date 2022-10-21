from django.http import HttpResponse
from rest_framework import viewsets
from .models import Game
from .serializers import GameSerializer
from rest_framework.decorators import action


# Create your views here.
def index(request):
    return HttpResponse("Game Route")


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
