"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from knox import views as knox_views
from it.views import LoginView

from .swagger import schema_view

urlpatterns = []

urlpatterns = [
    path("admin/", admin.site.urls),
    path(r"it/", include("it.urls")),
    # Authentication
    path(r"auth/login/", LoginView.as_view(), name="knox_login"),
    path(r"auth/logout/", knox_views.LogoutView.as_view(), name="knox_logout"),
    path(r"auth/logoutall/", knox_views.LogoutAllView.as_view(), name="knox_logoutall"),
]

# Documentation
urlpatterns += [
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
]
