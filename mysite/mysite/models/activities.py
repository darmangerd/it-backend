from django.db import models


class Activities(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=50)
    coefficient = models.FloatField()
