from django.http import JsonResponse
from rest_framework import viewsets
from .serializers import UserSerializer
from django.contrib.auth.models import User


def index(request):
    return JsonResponse({
        "users": True
    })


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("username")
    serializer_class = UserSerializer
