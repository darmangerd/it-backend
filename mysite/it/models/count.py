from django.db import models


class FoodCount(models.Model):
    name = models.CharField(max_length=50)
    count = models.IntegerField()
