from django.contrib import admin

# Register your models here.
from .models import Towers, BiminiImages, Biminis, Images


admin.site.register(Towers)
admin.site.register(Images)
admin.site.register(Biminis)
admin.site.register(BiminiImages)

