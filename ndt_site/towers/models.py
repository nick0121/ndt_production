from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

MANUFACTURERS = (
    ('1', 'Mastercraft'),
    ('2', 'Moomba'),
    ('3', 'Stingray'),
    ('4', 'Cobalt'),
    ('5', 'Bryant'),
    ('6', 'Four Winns'),
    ('7', 'Sea Doo'),
    ('8', 'Malibu'),
    ('9', 'Bayliner'),
    ('10', 'Startcraft'),
    ('11', 'Centurion'),
    ('12', 'Tige'),
    ('13', 'Nautique'),
    ('14', 'Yamaha'),
    ('15', 'Supra'),
)

IMAGES = (
    ('1', 'Main'),
    ('2', 'Angled'),
    ('3', 'Back'),
    ('4', 'Collapsed'),
)


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


# Create your models here.
class Towers(models.Model):

    title = models.CharField(max_length=200, unique=True)
    manufacturer = models.PositiveIntegerField(choices=MANUFACTURERS, default=None)
    start_year = models.PositiveIntegerField(default=current_year(), validators=[MinValueValidator(1970), max_value_current_year])
    end_year = models.PositiveIntegerField(default=current_year(), validators=[MinValueValidator(1970), max_value_current_year])
    model = models.CharField(max_length=20)
    price = models.DecimalField(max_length=7, max_digits=2, decimal_places=2)
    description = models.TextField(blank=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Towers"



class TowerOrder(models.Model):
    BRUSHED = 'Brushed'
    POWDER_COATED = 'Powder Coated'
    POLISHED = 'Polished'

    FINISHES = (
        ('BRUSHED', 'Brushed'),
        ('POWDER_COATED', 'Powder coated'),
        ('POLISHED', 'Polished'),
    )

    tower = models.ForeignKey(Towers, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    style = models.CharField(max_length=2, choices=(('FL', 'Fullsize'), ('MN', 'Mini')), default='Fullsize')
    finish = models.CharField(max_length=20, choices=FINISHES, default=BRUSHED)

    def __str__(self):
        return self.tower

    
    class Meta:
        verbose_name_plural = "TowerOrders"


class Biminis(models.Model):

    name = models.ForeignKey(Towers, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = "Biminis"


class BiminiOrder(models.Model):
    COLORS = (
        ('BK', 'Black'),
        ('JR', 'Jockey Red'),
        ('LR', 'Logo Red'),
        ('OR', 'Orange'),
        ('BD', 'Burgandy'),
        ('PB', 'Pacific Blue'),
        ('CD', 'Concord'),
        ('SY', 'Sunflower Yellow'),
        ('TQ', 'Turquoise'),
        ('SB', 'Sky Blue'),
        ('TS', 'Toast'),
        ('NT', 'Natural'),
        ('CG', 'Cadet Grey'),
        ('CL', 'Charcoal Grey'),
        ('BR', 'Brown'),
        ('NY', 'Navy'),
        ('FG', 'Forest Green'),
        ('RB', 'Royal Blue'),
        ('TN', 'Tan'),
        ('PG', 'Persian Green'),
    )

    bimini = models.ForeignKey(Biminis, on_delete=models.CASCADE)
    color = models.CharField(max_length=20, choices=COLORS, default=COLORS[0])
    qty = models.IntegerField(default=1)

    def __str__(self):
        return self.BiminiId


    class Meta:
        verbose_name_plural = "BiminiOrders"


class Images(models.Model):

    name = models.ForeignKey(Towers, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    manufacturer = models.PositiveIntegerField(choices=MANUFACTURERS, default=None)
    orientation = models.PositiveSmallIntegerField(choices=IMAGES, default=1)
    image = models.ImageField()

    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = "Images"

class BiminiImages(models.Model):

    name = models.ForeignKey(Biminis, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    manufacturer = models.PositiveIntegerField(choices=MANUFACTURERS, default=None)
    orientation = models.PositiveSmallIntegerField(choices=IMAGES, default=1)
    image = models.ImageField()

    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = "BiminiImages"