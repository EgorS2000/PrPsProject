# Generated by Django 3.0.4 on 2020-03-29 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RentCheck', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='table',
            options={'verbose_name': 'Таблица', 'verbose_name_plural': 'Таблицы'},
        ),
        migrations.AlterField(
            model_name='table',
            name='rented_rooms',
            field=models.IntegerField(verbose_name=0),
        ),
    ]