from django.db import models
from django_countries.fields import CountryField
from localflavor.us.us_states import STATE_CHOICES



class Customers(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=20)
    zipCode = models.CharField("Zip/Postal Code", max_length=20)
    country = CountryField(blank_label='(select country)')
    review = models.TextField(blank=True)

    def __str__(self):
        return self.last_name



## Dealers class
class Dealers(models.Model):
    
    name = models.CharField(max_length=30)
    dealer_of = models.CharField("Manufacturer", max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2, choices=STATE_CHOICES, null=True, blank=True)
    zipCode = models.CharField(max_length=50)
    contactName = models.CharField(max_length=30)
    has_ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.name



class PhoneNumbers(models.Model):

    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, null=True)
    dealer = models.ForeignKey(Dealers, on_delete=models.CASCADE, null=True)
    primaryNumber = models.IntegerField(blank=True, default=None)
    secondaryNumber = models.IntegerField(blank=True, default=None)

    def __str__(self):
        return self.customer


# Create your models here.
class Products(models.Model):

    name = models.CharField(max_length=30)
    price = models.DecimalField(max_length=7, max_digits=2, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class OrderProducts(models.Model):

    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.productId



class Orders(models.Model):

    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    dateOrdered = models.DateTimeField()
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.orderId


class Shipping(models.Model):

    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    dateOrdered = models.DateTimeField()
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.order

