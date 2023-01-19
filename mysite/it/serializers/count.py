from rest_framework import serializers
from ..models import FoodCount


class FoodCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCount
        fields = ["name", "count"]
