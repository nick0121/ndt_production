from django.db import models
from towers.models import Towers, TowerOrder
from localflavor.us.models import USStateField




class Customers(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.USStateField(_('state'), default=None)
    zipCode = models.CharField(max_length=20)
    review = models.TextField(blank=True)

    def __str__(self):
        return self.last_name



## Dealers class
class Dealers(models.Model):
    
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    city = models.CharField(_('city'), max_length=50)
    state = models.USStateField(_('state'), default=None)
    zipCode = models.CharField(max_length=50)
    contactName = models.CharField(max_length=30)
    has_ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.name



class PhoneNumbers(models.Model):

    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    dealer = models.ForeignKey(Dealers, on_delete=models.CASCADE)
    primaryNumber = models.IntegerField(default=0)
    secondaryNumber = models.IntegerField(blank=True)

    def __str__(self):
        return self.customerId


# Create your models here.
class Products(models.Model):

    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_length=7, max_digits=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class OrderProducts(models.Model):

    productId = models.ForeignKey(Products, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.productId



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

