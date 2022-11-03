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
    permission_classes = [permissions.IsAuthenticated | permissions.IsAdminUser]
    swagger_tag = ["Quantity"]
