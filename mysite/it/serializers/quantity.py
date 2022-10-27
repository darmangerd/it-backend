from ..models import Quantity
from rest_framework import serializers


class QuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Quantity
        fields = ["id", "gram", "id_food", "id_meal"]
