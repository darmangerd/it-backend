from django.db import models


class Food(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    energy_kcal = models.IntegerField()
    proteins_g = models.FloatField()
    lipids_g = models.FloatField()
    carbohydrates_g = models.FloatField()
