from django.db import models
import uuid

# Create your models here.
class Reflection(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, null=False, blank=True)

    key = models.CharField(max_length=50)
    value = models.CharField(max_length=50)

    def __str__(self):
        return self.key