from ..models import Client
from rest_framework import serializers


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ["user", "weight_kg", "height_cm", "gender"]
