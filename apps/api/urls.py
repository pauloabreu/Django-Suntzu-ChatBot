from rest_framework.routers import DefaultRouter, SimpleRouter
from apps.api.views import PairMessageViewSet, PairViewSet, ReflectionViewSet, ChatBotRespondAPIView
from django.urls import path, include
from django.conf.urls import url

app_name = 'api'

router = SimpleRouter()
router.register(r'reflection', ReflectionViewSet)
router.register(r'pair', PairViewSet)
router.register(r'pair_message', PairMessageViewSet)

urlpatterns = [
    path('respond', ChatBotRespondAPIView.as_view()),
]

urlpatterns += router.urls