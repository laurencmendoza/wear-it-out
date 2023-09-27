# Generated by Django 4.2.5 on 2023-09-27 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_color_user_tag_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('clothingitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.clothingitem')),
            ],
        ),
    ]