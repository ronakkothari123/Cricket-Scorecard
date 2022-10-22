from django.http import JsonResponse
from rest_framework import viewsets
from .serializers import UserSerializer, ProfileSerializer
from django.contrib.auth.models import User
from .models import Profile


def index(request):
    return JsonResponse({
        "users": True
    })


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("username")
    serializer_class = UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
