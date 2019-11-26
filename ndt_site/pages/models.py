from django.db import models
from django_countries.fields import CountryField
from localflavor.us.us_states import STATE_CHOICES
from phone_field import PhoneField





class Customers(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    review = models.TextField(blank=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


    class Meta:
        verbose_name_plural = "Customers"




## Dealers class
class Dealers(models.Model):
    
    name = models.CharField(max_length=30)
    dealer_of = models.CharField("Manufacturer", max_length=100)
    contactName = models.CharField(max_length=30)
    has_ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Dealers"



class Address(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, blank=True)
    dealer = models.ForeignKey(Dealers, on_delete=models.CASCADE, blank=True)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=20)
    zipCode = models.CharField("Zip/Postal Code", max_length=20)
    phone = PhoneField(blank=True, help_text='contact phone number')
    secondary_phone = PhoneField(blank=True, help_text='contact phone number')
    country = CountryField(blank_label='(select country)')
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.address1


    class Meta:
        verbose_name_plural = "Addresses"



# Create your models here.
class Products(models.Model):

    name = models.CharField(max_length=30)
    price = models.DecimalField(max_length=7, max_digits=2, decimal_places=2)
    image = models.ImageField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = "Products"



class Orders(models.Model):

    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    dateOrdered = models.DateTimeField()
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.customer


    class Meta:
        verbose_name_plural = "Orders"



class OrderDetails(models.Model):

    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.product


    class Meta:
        verbose_name_plural = "OrderDetails"


class Shipping(models.Model):

    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    dateOrdered = models.DateTimeField()
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.order


    class Meta:
        verbose_name = "Shipping"
