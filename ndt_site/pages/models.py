from django.db import models
from towers.models import Towers


# Create your models here.
class Products(models.Model):
    productId = models.AutoField(primary_key=True)
    towerId = models.ForeignKey(Towers, on_delete=models.CASCADE)
    productName = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    units = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.productName


class OrderProducts(models.Model):
    productId = models.ForeignKey(Products, on_delete=models.CASCADE)
    qtyEach = models.IntegerField(default=0)
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.orderId



class Customers(models.Model):
    CustomerId = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipCode = models.CharField(max_length=255)
    message = models.TextField(blank=True)
    review = models.TextField(blank=True)

    def __str__(self):
        return self.CustomerId


class Orders(models.Model):
    orderId = models.AutoField(primary_key=True)
    customerId = models.ForeignKey(Customers, on_delete=models.CASCADE)
    dateOrdered = models.DateTimeField()
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.orderId


class Shipping(models.Model):
    shippingId = models.AutoField(primary_key=True)
    orderId = models.ForeignKey(Orders, on_delete=models.CASCADE)
    dateOrdered = models.DateTimeField()
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.shippingId



class PhoneNumbers(models.Model):
    customerId = models.ForeignKey(Customers, on_delete=models.CASCADE)
    primaryNumber = models.IntegerField(default=0)
    secondaryNumber = models.IntegerField(blank=True)

    def __str__(self):
        return self.customerId

## Dealers class
class Dealers(models.Model):
    dealerId = models.AutoField(primary_key=True)
    dealerName = models.CharField(max_length=255)
    dealerClass = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipCode = models.CharField(max_length=255)
    phone = models.IntegerField(default=0)
    contactName = models.CharField(max_length=255)
    has_ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.dealerName