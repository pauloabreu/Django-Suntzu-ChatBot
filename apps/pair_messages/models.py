from django.db import models
import uuid
from apps.pairs.models import Pair

# Create your models here.
class PairMessage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, null=False, blank=True)
    pair = models.ForeignKey(Pair, on_delete=models.CASCADE)
    value = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.value