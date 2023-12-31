# Generated by Django 4.2.5 on 2023-09-26 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_color_clothingitem_colors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='clothingitem',
            name='tags',
            field=models.ManyToManyField(to='main_app.tag'),
        ),
    ]
