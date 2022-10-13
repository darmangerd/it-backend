from django.db import models

class Meals(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    foods = models.ManyToManyField(
        'Foods', 
        through='')
    users = models.ForeignKey(
        "Users",
        on_delete=models.CASCADE,
        )
