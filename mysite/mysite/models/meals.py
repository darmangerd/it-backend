from django.db import models


class Meals(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    id_user = models.ForeignKey(
        "Users",
        on_delete=models.CASCADE,
    )
