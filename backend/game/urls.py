from django.urls import path, include
from rest_framework import routers
from .views import GameViewSet

router = routers.DefaultRouter()
router.register("", GameViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
