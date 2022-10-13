from django.db import models


class Quantities(models.Model):
    id = models.AutoField(primary_key=True)
    gram = models.IntegerField()
    id_food = models.ForeignKey(
        "Foods",
        on_delete=models.CASCADE,
    )
    id_meal = models.ForeignKey(
        "Meals",
        on_delete=models.CASCADE,
    )
