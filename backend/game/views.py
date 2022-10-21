from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from .models import Game, ARCL
from .serializers import GameSerializer, ARCLSerializer
from rest_framework.decorators import action
from arcl_parser.functions import parse
from utils import parse_request


# Create your views here.
def index(request):
    return HttpResponse("Game Route")


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class ARCLGameViewSet(viewsets.ModelViewSet):
    queryset = ARCL.objects.all()
    serializer_class = ARCLSerializer

    def create(self, request, *args, **kwargs):
        body = parse_request(request)
        return JsonResponse(parse(body['url']))

