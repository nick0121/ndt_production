from django.db import models
from django_countries.fields import CountryField
from localflavor.us.us_states import STATE_CHOICES
from ndt_site.towers.models import MANUFACTURERS, TowerOrder, BiminiOrder




#CUSTOMER CLASS
class Customers(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    review = models.TextField(blank=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


    class Meta:
        verbose_name_plural = "Customers"




## DEALER CLASS
class Dealers(models.Model):
    
    name = models.CharField(max_length=30)
    dealer_of = models.CharField("Manufacturer", max_length=100, choices=MANUFACTURERS)
    contactName = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    has_ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Dealers"


# ADDRESS CLASS
class Address(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, blank=True, null=True)
    dealer = models.ForeignKey(Dealers, on_delete=models.CASCADE, blank=True, null=True)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=20)
    zipCode = models.CharField("Zip/Postal Code", max_length=20)
    phone = models.PositiveIntegerField(blank=False) ############################################## FIX PHONE FIELD ###############
    secondary_phone = models.PositiveIntegerField(blank=False)
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
    weight = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField(blank=True)
    sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=7, decimal_places=2, blank=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = "Products"



class Orders(models.Model):

    name = models.CharField(max_length=100)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    dateOrdered = models.DateTimeField()
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = "Orders"



class OrderDetails(models.Model):

    name = models.CharField(max_length=100)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    tower = models.ForeignKey(TowerOrder, on_delete=models.CASCADE, null=True, blank=True)
    bimini = models.ForeignKey(BiminiOrder, on_delete=models.CASCADE, null=True, blank=True)
    qty = models.IntegerField(default=1)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = "OrderDetails"
        unique_together = ('order', 'product')

class Shipping(models.Model):

    # name = models.CharField(max_length=100)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    dateOrdered = models.DateTimeField()
    weight = models.DecimalField(max_digits=7, decimal_places=2)
    comments = models.TextField(blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    # def __str__(self):
    #     return self.order


    class Meta:
        verbose_name = "Shipping"
