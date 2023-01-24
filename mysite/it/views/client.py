from rest_framework import viewsets
from rest_framework import permissions

from ..models import Client
from ..serializers import ClientSerializer
from ..permissions import IsOwner


class ClientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Meal to be viewed or edited.
    """

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    swagger_tag = ["Client"]

    def get_queryset(self):
        """
        Get client by id_user if provided
        else return all clients
        """
        id_user = self.request.query_params.get("id_user")
        if id_user:
            return Client.objects.filter(id_user=id_user)
        return Client.objects.all()
