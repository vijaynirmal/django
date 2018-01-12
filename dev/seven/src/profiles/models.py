from django.db import models
from django.utils import timezone

# Create your models here.

class Profile(models.Model) :
    name = models.CharField(max_length=120)
    description = models.TextField(max_length=500)
    email = models.CharField(max_length=120)
    added = models.DateTimeField('created',default=timezone.now())
    updated = models.DateTimeField('modified',  auto_now=True)


    def __str__(self):
        return self.name
