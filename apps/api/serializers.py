from rest_framework import serializers
from apps.pair_messages.models import PairMessage
from apps.pairs.models import Pair
from apps.reflections.models import Reflection

class ReflectionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Reflection
    fields = [
      'id',
      'key',
      'value'
    ]

class PairSerializer(serializers.ModelSerializer):
  class Meta:
    model = Pair
    fields = [
      'id',
      'key'
    ]

class PairMessageSerializer(serializers.ModelSerializer):
  class Meta:
    model = PairMessage
    fields = [
      'id',
      'value'
    ]