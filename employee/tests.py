from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from restaurants.models import Restaurant, Menu, Vote
from restaurants.serializers import RestaurantSerializer, MenuSerializer

RESTAURANTS_URL = reverse("restaurants:restaurants")
MENU_URL = reverse("restaurants:menus")


class UnauthenticatedApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_restaurants_list(self):
        res = self.client.get(RESTAURANTS_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_menu_list(self):
        res = self.client.get(MENU_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class AuthenticatedMovieApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            "test_user",
            "testtest11",
        )
        self.client.force_authenticate(self.user)

    def test_list_movies(self):
        Restaurant.objects.create(name="test_restaurant")

        response = self.client.get(RESTAURANTS_URL)

        restaurant = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurant, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_list_menu(self):
        restaurant = Restaurant.objects.create(name="test_restaurant")
        Menu.objects.create(
            restaurant_id=restaurant.id,
            content="test_content"
        )

        response = self.client.get(MENU_URL)

        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
