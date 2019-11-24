from django.db import models


# Create your models here.
class Towers(models.Model):
    FINISHES = (
        ('A', 'Anodized'),
        ('PC', 'Powder coated'),
        ('P', 'Polished'),
    )

    boatName = models.CharField(max_length=200)
    boatModel = models.CharField(max_length=100)
    style = models.CharField(max_length=100, default="fullsize")
    finish = models.CharField(max_length=100, choices=FINISHES, default=FINISHES[0])
    price = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    main_image = models.ImageField(blank=True)
    angled_Image = models.ImageField(blank=True)
    back_image = models.ImageField(blank=True)
    collapsed_image = models.ImageField(blank=True)

    def __str__(self):
        return self.boatName


class Biminis(models.Model):

    COLORS = (
        ('BK', 'Black'),
        ('RD', 'Red'),
        ('BL', 'Blue'),
        ('MR', 'Maroon'),
        ('BD', 'Burgandy'),
    )

    towerId = models.ForeignKey(Towers, on_delete=models.CASCADE)
    color = models.CharField(max_length=100, choices=COLORS)
    price = models.IntegerField()

    def __str__(self):
        return self.towerId



class ModelYear(models.Model):
    modelId = models.AutoField(primary_key=True)
    towerId = models.ForeignKey(Towers, on_delete=models.CASCADE)
    m_year = models.IntegerField()




