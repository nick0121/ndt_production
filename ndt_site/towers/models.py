from django.db import models


# Create your models here.
class Towers(models.Model):
    FINISHES = (
        ('A', 'Anodized'),
        ('PC', 'Powder coated'),
        ('P', 'Polished'),
    )

    # towerId = models.AutoField(primary_key=True)
    boatName = models.CharField(max_length=100, default="mastercraft")
    boatModel = models.CharField(max_length=100, default="prostar")
    style = models.CharField(max_length=100, default="fullsize")
    finish = models.CharField(max_length=100, choices=FINISHES, default=FINISHES[0])
    price = models.IntegerField(default=0)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.towerId


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
    color = models.CharField(max_length=100, choices=COLORS)
    price = models.IntegerField()

    def __str__(self):
        return self.biminiId


class Images(models.Model):
    imageId = models.AutoField(primary_key=True)
    towerId = models.ForeignKey(Towers, on_delete=models.CASCADE)
    profile = models.ImageField()
    angled = models.ImageField()
    collapsed = models.ImageField()
    back = models.ImageField()

    def __str__(self):
        return self.imageId


class ModelYear(models.Model):
    modelId = models.AutoField(primary_key=True)
    towerId = models.ForeignKey(Towers, on_delete=models.CASCADE)
    m_year = models.IntegerField()




