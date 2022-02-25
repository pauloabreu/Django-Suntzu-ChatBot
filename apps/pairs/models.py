from django.db import models
from django.contrib.postgres.fields import ArrayField
import uuid

# Create your models here.
class Pair(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, null=False, blank=True)

    key = models.CharField(max_length=100)

    def __str__(self):
        return self.key