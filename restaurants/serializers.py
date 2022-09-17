from rest_framework import serializers

from restaurants.models import Drink, Dish, Menu, Restaurant, Vote


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = "__all__"


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = "__all__"


class MenuSerializer(serializers.ModelSerializer):
    drinks = DrinkSerializer(many=True)
    dishes = DishSerializer(many=True)

    class Meta:
        model = Menu
        fields = ("id", "drinks", "dishes", "votes")


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = "__all__"
