import datetime

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication

from restaurants.models import Drink, Dish, Menu, Restaurant, Vote
from restaurants.serializers import (
    DrinkSerializer,
    DishSerializer,
    MenuSerializer,
    RestaurantSerializer,
    VoteSerializer,
)


class DrinkViewSet(viewsets.ModelViewSet):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
    permission_classes = (IsAdminUser,)


class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = (IsAdminUser,)


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = (IsAuthenticated,)

    @action(
        methods=["GET"],
        detail=False,
        url_path="selected",
        permission_classes=[IsAuthenticated],
    )
    def menu_for_today(self):
        try:
            return Menu.objects.order_by("-votes")[0]
        except IndexError:
            return "No menus yet."


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = (IsAuthenticated,)


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = (IsAuthenticated,)
