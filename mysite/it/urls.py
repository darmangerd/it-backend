from django.urls import include, path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"client", views.ClientViewSet)
router.register(r"food", views.FoodViewSet)
router.register(r"meal", views.MealViewSet)
router.register(r"quantity", views.QuantityViewSet)
router.register(r"users", views.UserViewSet)
router.register(r"foodcount", views.FoodCountViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
