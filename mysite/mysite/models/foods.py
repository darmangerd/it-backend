from django.db import models


class Foods(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    energy_kcal = models.IntegerField()
    proteins_g = models.FloatField()
    carbohydrates_g = models.FloatField()
    lipids_g = models.FloatField()
