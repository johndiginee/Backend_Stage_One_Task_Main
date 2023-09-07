from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EndpointDataViewSet

router = DefaultRouter()
router.register(r'api', EndpointDataViewSet, basename='api')

urlpatterns = [
    path('', include(router.urls)),
]
