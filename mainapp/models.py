from django.db import models

class Planet(models.Model):
    name = models.CharField(max_length=100)
    temp = models.CharField(max_length=100)
    hrs = models.CharField(max_length=100)
    mass = models.CharField(max_length=100)
    diameter = models.CharField(max_length=100)
    circumference = models.CharField(max_length=100)

