from django.db import models
from django.utils import timezone


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    location = models.CharField(max_length=255, default="None")
    reorderpoint = models.CharField(max_length=255, default="None")
    brand = models.CharField(max_length=255, default="None")
    created_at = models.DateTimeField(auto_now_add=True)
    expirationdate = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Admin(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
