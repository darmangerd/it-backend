from django.contrib.auth import login
from django.contrib.auth.models import User

from rest_framework import viewsets, permissions
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer

from knox.views import LoginView as KnoxLoginView

from ..serializers import UserSerializer

from drf_yasg.utils import swagger_auto_schema


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    swagger_tag = ["User"]


class LoginView(KnoxLoginView):
    """
    API endpoint allowing the user to login and receive a token
    """

    permission_classes = [
        permissions.AllowAny,
    ]

    @swagger_auto_schema(request_body=AuthTokenSerializer)
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        return super(LoginView, self).post(request, format=None)
