from django.contrib import admin

# Register your models here.
from .models import Towers, Biminis, Images, TowerOrder, BiminiOrder


admin.site.register(Towers)
admin.site.register(Images)
admin.site.register(Biminis)
admin.site.register(TowerOrder)
admin.site.register(BiminiOrder)

