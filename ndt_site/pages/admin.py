from django.contrib import admin

from .models import Products, Orders, Customers, Dealers
# Register your models here.


admin.site.register(Customers)
admin.site.register(Dealers)
admin.site.register(Products)
admin.site.register(Orders)


