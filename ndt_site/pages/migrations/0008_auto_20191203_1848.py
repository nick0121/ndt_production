# Generated by Django 2.2.7 on 2019-12-03 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_auto_20191202_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealers',
            name='dealer_of',
            field=models.CharField(choices=[('none', 'select a manufacturer'), ('mastercraft', 'Mastercraft'), ('moomba', 'Moomba'), ('stingray', 'Stingray'), ('cobalt', 'Cobalt'), ('bryant', 'Bryant'), ('four winns', 'Four Winns'), ('sea doo', 'Sea Doo'), ('malibu', 'Malibu'), ('bayliner', 'Bayliner'), ('starcraft', 'Startcraft'), ('centurion', 'Centurion'), ('tige', 'Tige'), ('nautique', 'Nautique'), ('yamaha', 'Yamaha'), ('supra', 'Supra'), ('not_listed', 'Not Listed')], max_length=100, verbose_name='Manufacturer'),
        ),
    ]
