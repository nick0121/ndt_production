from django.db import models


# Create your models here.
class Towers(models.Model):
    FINISHES = (
        ('A', 'Anodized'),
        ('PC', 'Powder coated'),
        ('P', 'Polished'),
    )

    towerId = models.AutoField(primary_key=True)
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    boatName = models.CharField(max_length=20)
    boatModel = models.CharField(max_length=20)
    style = models.CharField(max_length=20)
    finish = models.CharField(max_length=2, choices=FINISHES)
    price = models.IntegerField()
    description = models.TextField(blank=True)


class Biminis(models.Model):

    COLORS = (
        ('BK', 'Black'),
        ('RD', 'Red'),
        ('BL', 'Blue'),
        ('MR', 'Maroon'),
        ('BD', 'Burgandy'),
    )

    biminiId = models.AutoField(primary_key=True)
    towerId = models.ForeignKey(Towers, on_delete=models.CASCADE)
    color = models.CharField(max_length=2, choices=COLORS)
    price = models.IntegerField()


class Images(models.Model):
    imageId = models.AutoField(primary_key=True)
    towerId = models.ForeignKey(Towers, on_delete=models.CASCADE)
    profile = models.ImageField()
    angled = models.ImageField()
    collapsed = models.ImageField()
    back = models.ImageField()


class ModelYear(models.Model):
    modelId = models.AutoField(primary_key=True)
    towerId = models.ForeignKey(Towers, on_delete=models.CASCADE)
    m__year = models.IntegerField()




