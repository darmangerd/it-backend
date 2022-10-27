from rest_framework import viewsets
from rest_framework import permissions

from ..models import Client
from ..serializers import ClientSerializer


class ClientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Meal to be viewed or edited.
    """

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]
    swagger_tag = ["Client"]
