from rest_framework import viewsets
from rest_framework import permissions
from django.db.models import Count

from ..models import Food, Quantity, Meal, Client, FoodCount
from ..serializers import FoodCountSerializer


class FoodCountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows food count to be viewed or edited.
    """

    queryset = FoodCount.objects.all()
    serializer_class = FoodCountSerializer

    def get_queryset(self):
        """
        Get the top 10 food by count
        """
        queryset = (
            Quantity.objects.values("id_food__name")
            .annotate(count=Count("id_food__name"))
            .order_by("-count")[:10]
        )
        food_count = []
        for item in queryset:
            food_count.append(
                FoodCount(name=item["id_food__name"], count=item["count"])
            )
        return food_count
