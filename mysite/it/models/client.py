from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    weight_kg = models.IntegerField()
    height_cm = models.IntegerField()
    gender = models.CharField(max_length=1)
