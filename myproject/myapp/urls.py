from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArtistViewSet, WorkViewSet

router = DefaultRouter()
router.register(r'artists', ArtistViewSet)
router.register(r'works', WorkViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
