from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("user/", include("users.urls")),
    path("game/", include("game.urls")),
    path("teams/", include("teams.urls"))
]
