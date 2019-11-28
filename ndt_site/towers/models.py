from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator


MANUFACTURERS = (
    ('none', 'None'),
    ('mastercraft', 'Mastercraft'),
    ('moomba', 'Moomba'),
    ('stingray', 'Stingray'),
    ('cobalt', 'Cobalt'),
    ('bryant', 'Bryant'),
    ('four winns', 'Four Winns'),
    ('sea doo', 'Sea Doo'),
    ('malibu', 'Malibu'),
    ('bayliner', 'Bayliner'),
    ('starcraft', 'Startcraft'),
    ('centurion', 'Centurion'),
    ('tige', 'Tige'),
    ('nautique', 'Nautique'),
    ('yamaha', 'Yamaha'),
    ('supra', 'Supra'),
)



def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


# Create your models here.
class Towers(models.Model):

    title = models.CharField(max_length=200, unique=True)
    manufacturer = models.CharField(choices=MANUFACTURERS, default=None, max_length=50)
    start_year = models.PositiveIntegerField(default=current_year(), validators=[MinValueValidator(1970), max_value_current_year])
    end_year = models.PositiveIntegerField(default=current_year(), validators=[MinValueValidator(1970), max_value_current_year])
    model = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
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

    name = models.CharField(max_length=100)
    tower = models.ForeignKey(Towers, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    style = models.CharField(max_length=2, choices=(('FL', 'Fullsize'), ('MN', 'Mini')), default='Fullsize')
    finish = models.CharField(max_length=20, choices=FINISHES, default=BRUSHED)

    def __str__(self):
        return self.name

    
    class Meta:
        verbose_name_plural = "TowerOrders"


class Biminis(models.Model):

    name = models.CharField(max_length=100)
    tower = models.ForeignKey(Towers, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
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

    name = models.CharField(max_length=100)
    bimini = models.ForeignKey(Biminis, on_delete=models.CASCADE)
    color = models.CharField(max_length=20, choices=COLORS, default=COLORS[0])
    qty = models.IntegerField(default=1)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = "BiminiOrders"


class Images(models.Model):

    ORIENTATIONS = (
        ('main', 'Main'),
        ('angled', 'Angled'),
        ('back', 'Back'),
        ('collapsed', 'Collapsed'),
    )

    title = models.CharField(max_length=100)
    tower = models.ForeignKey(Towers, on_delete=models.CASCADE, blank=True, null=True, default=None)
    product = models.ForeignKey('pages.Products', on_delete=models.CASCADE, blank=True, null=True, default=None)
    description = models.TextField(blank=True)
    manufacturer = models.CharField(choices=MANUFACTURERS, default=None, max_length=50)
    image = models.ImageField(upload_to='photos/')
    orientation = models.CharField(max_length=20, blank=True, default=None, choices=ORIENTATIONS)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name_plural = "Images"

