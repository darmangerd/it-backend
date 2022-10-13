from django.db import models
from mysite.mysite.models import activities


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    weight_kg = models.IntegerField()
    height_cm = models.IntegerField()
    sexe = models.CharField(max_length=1)
    activities = models.ForeignKey(
        "Activities",
        on_delete=models.CASCADE,
    )
