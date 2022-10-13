from django.db import models


class Meal(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    id_user = models.ForeignKey(
        "Client",
        on_delete=models.CASCADE,
    )
