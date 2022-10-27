from django.contrib.auth import login
from django.contrib.auth.models import User

from rest_framework import viewsets, permissions
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer

# from knox.views import LoginView as KnoxLoginView

from ..serializers import UserSerializer

# from drf_yasg.utils import swagger_auto_schema


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    swagger_tag = ["User"]
