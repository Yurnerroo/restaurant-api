from django.urls import path, include
from rest_framework import routers

from restaurants.views import MenuViewSet, RestaurantViewSet, DrinkViewSet, DishViewSet, VoteViewSet

router = routers.DefaultRouter()
router.register("menus", MenuViewSet)
router.register("drinks", DrinkViewSet)
router.register("dishes", DishViewSet)
router.register("restaurants", RestaurantViewSet)
router.register("votes", VoteViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "restaurants"
