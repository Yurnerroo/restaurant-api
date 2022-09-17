from restaurant_service import settings
from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Drink(models.Model):
    name = models.CharField(max_length=100, null=False)
    price = models.FloatField(null=False)

    class Meta:
        unique_together = ("name", "price")

    def __str__(self):
        return f"{self.name} ({round(self.price, 2)}hrn.)"


class Dish(models.Model):
    name = models.CharField(max_length=100, null=False)
    price = models.FloatField(null=False)
    ingredients = models.CharField(max_length=200, null=False)

    class Meta:
        unique_together = ("name", "price")

    def __str__(self):
        return f"{self.name} ({round(self.price, 2)}hrn.): {self.ingredients}"


class Menu(models.Model):
    votes = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True)
    drinks = models.ManyToManyField(Drink, related_name="menus")
    dishes = models.ManyToManyField(Dish, related_name="menus")

    def __str__(self):
        return f"{self.restaurant.name}'s menu"

    class Meta:
        ordering = ["-votes", "date_created"]   # ordering by "-votes" means menu's rating


class Vote(models.Model):
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True
        )
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user_id", "menu_id")

    def __str__(self):
        return f"{self.user_id.name}: {self.menu_id.restaurant.name}'s menu"
