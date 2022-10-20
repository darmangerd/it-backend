from django.db import models
from django.contrib.auth.models import User


class Meal(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    id_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
