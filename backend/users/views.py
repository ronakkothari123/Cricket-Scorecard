import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return JsonResponse({
        "users": True
    })


@csrf_exempt
def register(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        content = body
        username, email, password = content['username'], content['email'], content['password']

        user = User.objects.create_user(username, email, password)
        user.save()
        return JsonResponse({
            "success": True,
            "username": user.username
        })

    return JsonResponse({
        "error": "invalid request method"
    })
