# Generated by Django 2.2.7 on 2019-11-30 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('towers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='tower',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='towers.Towers'),
        ),
        migrations.AlterField(
            model_name='towers',
            name='description',
            field=models.TextField(),
        ),
    ]