from rest_framework import viewsets
from rest_framework import permissions

from ..models import Food
from ..serializers import FoodSerializer


class FoodViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Food to be viewed or edited.
    """

    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [permissions.IsAuthenticated]
    swagger_tag = ["Food"]
