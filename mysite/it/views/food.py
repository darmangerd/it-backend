from rest_framework import viewsets
from rest_framework import permissions

from ..models import Food
from ..serializers import FoodSerializer
from ..permissions import IsOwner, IsStaffOrReadOnly


class FoodViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Food to be viewed or edited.
    """

    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.IsAuthenticated, IsOwner | IsStaffOrReadOnly]
    swagger_tag = ["Food"]

    def get_queryset(self):
        food_id = self.request.query_params.getlist("id")
        print(food_id)
        if food_id:
            return Food.objects.filter(id__in=food_id)
        return Food.objects.all()
