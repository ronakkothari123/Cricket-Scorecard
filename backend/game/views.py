from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from utils import parse_request
from .models import Game


# Create your views here.
def index(request):
    return HttpResponse("Game Route")


@csrf_exempt
def create_game(request):
    if request.method != "POST":
        return JsonResponse({
            "error": "Incorrect request method. Use `POST` instead."
        })

    body = parse_request(request)

    league_type = body['leagueType']
    league_types = ['A', 'O']

    if league_type not in league_types:
        return JsonResponse({
            "error": "Invalid `league_type` value. `league_type` must either be `A` or `O`."
        })

    game = Game(ball_by_ball=body['ballByBall'], league_type=league_types.index(league_type))
    game.save()

    return JsonResponse({
        "success": True
    })

