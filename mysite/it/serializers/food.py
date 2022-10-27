from ..models import Food
from rest_framework import serializers


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = [
            "id",
            "name",
            "energy_kcal",
            "proteins_g",
            "lipids_g",
            "carbohydrates_g",
        ]
