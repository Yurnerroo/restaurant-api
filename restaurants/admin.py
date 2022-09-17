from django.contrib import admin

from restaurants.models import Dish, Drink, Menu, Restaurant

admin.site.register(Dish)
admin.site.register(Drink)
admin.site.register(Menu)
admin.site.register(Restaurant)
