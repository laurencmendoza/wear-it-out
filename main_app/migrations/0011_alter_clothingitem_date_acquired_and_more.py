# Generated by Django 4.2.5 on 2023-09-29 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothingitem',
            name='date_acquired',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='clothingitem',
            name='place_purchased',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='clothingitem',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='clothingitem',
            name='size',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
