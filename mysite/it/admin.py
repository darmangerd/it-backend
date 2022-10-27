from django.contrib import admin
from .models import Client, Meal, Food, Quantity


admin.site.register(Client)
admin.site.register(Meal)
admin.site.register(Food)
admin.site.register(Quantity)
