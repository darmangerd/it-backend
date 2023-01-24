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
        """
        Get meal by id_user and date if provided
        else if only id_user is provided return all meals for this user
        else return all meals
        """
        user_id = self.request.query_params.get("id_user")
        datetime = self.request.query_params.get("date")
        if user_id is not None and datetime is not None:
            return Meal.objects.filter(id_user=user_id, date=datetime)
        if user_id is not None:
            return Meal.objects.filter(id_user=user_id)
        return Meal.objects.all()
