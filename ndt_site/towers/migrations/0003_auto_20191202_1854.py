# Generated by Django 2.2.7 on 2019-12-02 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('towers', '0002_auto_20191130_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='manufacturer',
            field=models.CharField(choices=[('none', 'None'), ('mastercraft', 'Mastercraft'), ('moomba', 'Moomba'), ('stingray', 'Stingray'), ('cobalt', 'Cobalt'), ('bryant', 'Bryant'), ('four winns', 'Four Winns'), ('sea doo', 'Sea Doo'), ('malibu', 'Malibu'), ('bayliner', 'Bayliner'), ('starcraft', 'Startcraft'), ('centurion', 'Centurion'), ('tige', 'Tige'), ('nautique', 'Nautique'), ('yamaha', 'Yamaha'), ('supra', 'Supra'), ('not_here', 'Not Here')], default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='towers',
            name='manufacturer',
            field=models.CharField(choices=[('none', 'None'), ('mastercraft', 'Mastercraft'), ('moomba', 'Moomba'), ('stingray', 'Stingray'), ('cobalt', 'Cobalt'), ('bryant', 'Bryant'), ('four winns', 'Four Winns'), ('sea doo', 'Sea Doo'), ('malibu', 'Malibu'), ('bayliner', 'Bayliner'), ('starcraft', 'Startcraft'), ('centurion', 'Centurion'), ('tige', 'Tige'), ('nautique', 'Nautique'), ('yamaha', 'Yamaha'), ('supra', 'Supra'), ('not_here', 'Not Here')], default=None, max_length=50),
        ),
    ]