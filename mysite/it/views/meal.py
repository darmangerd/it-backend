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

    def get_queryset(self):
        user_id = self.request.query_params.get("id")
        date = self.request.query_params.get("date")
        if user_id and date:
            return Meal.objects.filter(id_user=user_id, date=date)
        if user_id:
            return Meal.objects.filter(id_user=user_id)
        return Meal.objects.all()
