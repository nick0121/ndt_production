from django.db import models


# Create your models here.
class Towers(models.Model):

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

    title = models.CharField(max_length=200)
    manufacturer = models.PositiveIntegerField(choices=MANUFACTURERS, default=None)
    model = models.CharField(max_length=20)
    price = models.DecimalField(max_length=7, max_digits=2, default=None)
    description = models.TextField(blank=True)


    def __str__(self):
        return self.title



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
    towerId = models.ForeignKey(Towers, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    style = models.CharField(max_length=2, choices=(('FL', 'Fullsize'), ('MN', 'Mini')), default='Fullsize')
    finish = models.CharField(max_length=20, choices=FINISHES, default=BRUSHED)


class Biminis(models.Model):
    main_image = models.ImageField(blank=True)
    angled_Image = models.ImageField(blank=True)
    back_image = models.ImageField(blank=True)
    collapsed_image = models.ImageField(blank=True)
    name = models.CharField(max_length=100)
    towerId = models.ForeignKey(Towers, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name


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

    BiminiId = models.ForeignKey(Biminis, on_delete=models.CASCADE)
    color = models.CharField(max_length=20, choices=COLORS, default=COLORS[0])
    qty = models.IntegerField(default=1)

    def __str__(self);
        return self.BiminiId



class ModelYear(models.Model):
    towerId = models.ForeignKey(Towers, on_delete=models.CASCADE)
    m_year = models.IntegerField()



class Images(models.Model):

    IMAGES = (
        ('1', 'Main'),
        ('2', 'Angled'),
        ('3', 'Back'),
        ('4', 'Collapsed'),
    )

    tower_id = models.ForeignKey(Towers, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    manufacturer = models.CharField(max_length=30)
    orientation = models.PositiveSmallIntegerField(choices=IMAGES, default=1)

