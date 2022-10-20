from django.urls import path
from .views import index, create_game

urlpatterns = [
    path("", index, name='index'),
    path("create/", create_game, name='create_game')
]