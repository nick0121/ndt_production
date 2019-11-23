from django.db import models
from towers.models import Towers

# Create your models here.
class Products(models.Model):
    productId = models.AutoField(primary_key=True)
    towerId = models.ForeignKey(Towers, on_delete=models.CASCADE)
    productName = models.CharField(max_length=100)
    description = models.TextField()
    units = models.IntegerField()
    price = models.IntegerField()
    comments = models.TextField()

    def __str__(self):
        return self.productName


class OrderProducts(models.Model):
    orderId = models.ForeignKey(Products, on_delete=models.CASCADE)
    productId = models.ForeignKey(Products, on_delete=models.CASCADE)
    qtyEach = models.IntegerField()
    comments = models.TextField()



class Orders(models.Model):
    orderId = models.AutoField(primary_key=True)
    customerId = models.ForeignKey(Customers, on_delete=models.CASCADE)
    dateOrdered = models.DateTimeField()
    comments = models.TextField()

    def __str__(self):
        return self.orderId


class Shipping(models.Model):
    shippingId = models.AutoField(primary_key=True)
    orderId = models.ForeignKey(Orders, on_delete=models.CASCADE)
    dateOrdered = models.DateTimeField()
    comments = models.TextField()


class Customers(models.Model):
    CustomerId = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zipCode = models.CharField(max_length=10)
    message = models.TextField()
    review = models.TextField()


class PhoneNumbers(models.Model):
    customerId = models.ForeignKey(Customers, on_delete=models.CASCADE)
    primaryNumber = models.IntegerField()
    secondaryNumber = models.IntegerField()

## Dealers class
class Dealers(models.Model):
    dealerId = models.AutoField(primary_key=True)
    dealerName = models.CharField(max_length=20)
    dealerClass = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zipCode = models.CharField(max_length=20)
    phone = models.IntegerField()
    contactName = models.CharField(max_length=20)
    has__ordered = models.BooleanField()

    def __str__(self):
        return self.dealerName