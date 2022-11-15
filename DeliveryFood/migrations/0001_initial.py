# Generated by Django 4.1.1 on 2022-09-13 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Имя категории', max_length=100, verbose_name='name_cat')),
            ],
            options={
                'verbose_name': 'Category',
                'db_table': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Foods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Имя блюда', max_length=100, verbose_name='name_food')),
                ('description', models.TextField(blank=True, help_text='Описание блюда', max_length=1000, null=True, verbose_name='descr')),
                ('cost', models.IntegerField(help_text='Цена блюда', verbose_name='cost')),
                ('category', models.ForeignKey(help_text='ID категории', on_delete=django.db.models.deletion.CASCADE, to='DeliveryFood.categories', verbose_name='category')),
            ],
            options={
                'verbose_name': 'Food',
                'db_table': 'Foods',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foods', models.ManyToManyField(to='DeliveryFood.foods')),
                ('user', models.ForeignKey(help_text='ID пользователя', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Order',
                'db_table': 'Orders',
            },
        ),
    ]