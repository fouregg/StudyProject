# Generated by Django 4.1.1 on 2022-09-20 08:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DeliveryFood', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='dateorder',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='Дата заказа'),
        ),
        migrations.AddField(
            model_name='orders',
            name='pay',
            field=models.CharField(choices=[('POINT', 'Баллами'), ('MONEY', 'Наличиным'), ('CARD', 'Картой')], default='CARD', help_text='Тип оплаты', max_length=5),
        ),
    ]
