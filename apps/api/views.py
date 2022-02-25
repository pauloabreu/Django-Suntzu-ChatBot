from rest_framework import viewsets, permissions
from apps.chatbot_manager.manager import ChatBotManager
from apps.reflections.models import Reflection
from apps.pairs.models import Pair
from apps.pair_messages.models import PairMessage
from apps.api.serializers import PairMessageSerializer, PairSerializer, ReflectionSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from django.http import JsonResponse

# Create your views here.
class ReflectionViewSet(viewsets.ModelViewSet):
  queryset = Reflection.objects.all()
  serializer_class = ReflectionSerializer
  permission_classes = [permissions.AllowAny]

class PairViewSet(viewsets.ModelViewSet):
  queryset = Pair.objects.all()
  serializer_class = PairSerializer
  permission_classes = [permissions.AllowAny]

class PairMessageViewSet(viewsets.ModelViewSet):
  queryset = PairMessage.objects.all()
  serializer_class = PairMessageSerializer
  permission_classes = [permissions.AllowAny]

class ChatBotRespondAPIView(APIView):
  permission_classes = [permissions.AllowAny]

  def get(self, request, *args, **kwargs):
    return Response(ChatBotManager.respond(request.query_params['text']))
