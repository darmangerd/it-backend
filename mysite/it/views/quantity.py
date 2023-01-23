from rest_framework import viewsets
from rest_framework import permissions

from ..models import Quantity
from ..serializers import QuantitySerializer


class QuantityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Quantity to be viewed or edited.
    """

    queryset = Quantity.objects.all()
    serializer_class = QuantitySerializer
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.IsAuthenticated]
    swagger_tag = ["Quantity"]

    def get_queryset(self):
        id_meal = self.request.query_params.get("id_meal")
        if id_meal:
            return Quantity.objects.filter(id_meal=id_meal)
        return Quantity.objects.all()
