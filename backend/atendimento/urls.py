from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProtocoloAtendimentoModelViewSet


router = DefaultRouter()
router.register('protocolo', ProtocoloAtendimentoModelViewSet)


urlpatterns = [
    path('', include(router.urls))
]