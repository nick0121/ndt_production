from django.db import models

# Create your models here.
class Towers(models.Model):
    title = models.CharField(max_length=200)