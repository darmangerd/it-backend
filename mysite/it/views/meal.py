from rest_framework import viewsets
from rest_framework import permissions

from ..models import Meal
from ..serializers import MealSerializer


class MealViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Meal to be viewed or edited.
    """

    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = [permissions.IsAuthenticated]
    swagger_tag = ["Meal"]