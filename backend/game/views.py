from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from .models import Game
from .serializers import GameSerializer
from arcl_parser.functions import parse
from utils import parse_request


# Create your views here.
def index(request):
    return HttpResponse("Game Route")


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def create(self, request, *args, **kwargs):
        body = parse_request(request)
        if body['arcl']:
            return JsonResponse(parse(body['url']))
        super(GameViewSet, self).create(request, *args, **kwargs)


