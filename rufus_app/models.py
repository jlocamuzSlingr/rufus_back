# Create your models here.
from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='staticfiles/rest_framework/img/', default='')

class DishItem(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(blank=True, null=True)
    pictogram_id = models.CharField(max_length=255, blank=True)

class Dish(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='dishes', default=None)
    dish_items = models.ManyToManyField(DishItem, related_name='dishes', blank=True)


