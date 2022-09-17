# Generated by Django 4.1.1 on 2022-09-17 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurants", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="menu",
            name="dishes",
        ),
        migrations.RemoveField(
            model_name="menu",
            name="drinks",
        ),
        migrations.AddField(
            model_name="dish",
            name="menus",
            field=models.ManyToManyField(related_name="dishes", to="restaurants.menu"),
        ),
        migrations.AddField(
            model_name="drink",
            name="menus",
            field=models.ManyToManyField(related_name="drinks", to="restaurants.menu"),
        ),
    ]
