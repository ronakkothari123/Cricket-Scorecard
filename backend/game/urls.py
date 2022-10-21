from django.urls import path, include
from rest_framework import routers
from .views import GameViewSet, ARCLGameViewSet

router = routers.DefaultRouter()
router.register("", GameViewSet)

router2 = routers.DefaultRouter()
router2.register("", ARCLGameViewSet)

urlpatterns = [
    path("std/", include(router.urls)),
    path("arcl/", include(router2.urls))
]
