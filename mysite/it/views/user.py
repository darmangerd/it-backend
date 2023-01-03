from django.contrib.auth import login
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer

from knox.views import LoginView as KnoxLoginView

from ..serializers import UserSerializer

from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth.models import User


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    swagger_tag = ["User"]

    # return the pk from the username
    def get_queryset(self):
        username = self.request.query_params.get("username")
        queryset = User.objects.all()
        if username:
            queryset = queryset.filter(username=username)
            # return pk
            return queryset.values("id", "username")
        return queryset

    # def list(self, request):
    #     username = request.query_params.get("username")
    #     if username:
    #         queryset = self.queryset.filter(username=username)
    #     else:
    #         queryset = self.queryset
    #     serializer = self.serializer_class(queryset, many=True)
    #     return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     try:
    #         user = self.queryset.get(pk=pk)
    #         serializer = self.serializer_class(user)
    #         return Response(serializer.data)

    #     except User.DoesNotExist:
    #         return Response({})


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
