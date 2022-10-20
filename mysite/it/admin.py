from django.contrib import admin
from .models import Client, Meal, Food, Quantity


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Meal._meta.get_fields()]


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Client._meta.get_fields()]


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Food._meta.get_fields()]


@admin.register(Quantity)
class QuantityAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Quantity._meta.get_fields()]
