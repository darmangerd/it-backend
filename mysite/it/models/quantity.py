from django.db import models


class Quantity(models.Model):
    id = models.AutoField(primary_key=True)
    gram = models.IntegerField()
    id_food = models.ForeignKey(
        "Food",
        on_delete=models.CASCADE,
    )
    id_meal = models.ForeignKey(
        "Meal",
        on_delete=models.CASCADE,
    )
