from django.db import models

from django.urls import reverse


class Cake(models.Model):
    name = models.CharField(max_length=250, unique=True)

class City(models.Model):
    name = models.CharField(max_length=128)


class Town(models.Model):
    name = models.CharField(max_length=128)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='towns')

