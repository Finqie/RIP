# Generated by Django 3.1.5 on 2021-01-13 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20210113_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='dealer',
            name='number',
            field=models.CharField(default=1, max_length=50),
        ),
        migrations.AlterField(
            model_name='car_model',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Название модели'),
        ),
    ]
