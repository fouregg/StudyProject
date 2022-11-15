from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime


class Categories(models.Model):
    name = models.CharField(max_length=100, blank=False, verbose_name="name_cat", null=False, help_text="Имя категории")

    class Meta:
        db_table = "Categories"
        verbose_name = "Category"

    def __str__(self):
        return self.name


class Foods(models.Model):
    category = models.ForeignKey(Categories, blank=False, null=False, on_delete=models.CASCADE, verbose_name="category",
                                 help_text="ID категории")
    name = models.CharField(max_length=100, blank=False, verbose_name="name_food", null=False, help_text="Имя блюда")
    description = models.TextField(max_length=1000, blank=True, verbose_name="descr", null=True,
                                   help_text="Описание блюда")
    cost = models.IntegerField(blank=False, null=False, verbose_name="cost", help_text="Цена блюда")

    class Meta:
        db_table = "Foods"
        verbose_name = "Food"

    def __str__(self):
        return self.name + " | " + str(self.category.name)

class Orders(models.Model):
    CARD = 'CARD'
    POINTS = 'POINT'
    MONEY = 'MONEY'
    CHOISES_PAY = [
        (POINTS, "Баллами"),
        (MONEY, "Наличиным"),
        (CARD, "Картой"),
    ]


    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE, help_text="ID пользователя")
    foods = models.ManyToManyField(Foods)
    pay = models.CharField(choices=CHOISES_PAY, max_length=5, default=CARD, help_text="Тип оплаты")
    dateorder = models.DateTimeField(blank=False, null=False, help_text="Дата заказа", default=datetime(2000,1,1))

    class Meta:
        db_table = "Orders"
        verbose_name = "Order"

    def __str__(self):
        return str(self.id) + " | " + self.pay

class Adress(models.Model):
    user_id = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE, help_text="ID пользователя")
    street = models.CharField(max_length=50, blank=False, verbose_name="name_street", null=False, help_text="Улица")
    build = models.CharField(max_length=50, blank=False, verbose_name="name_build", null=False, help_text="Дом")
    flat = models.IntegerField( blank=False, verbose_name="name_flat", null=False, help_text="Квартира")

    class Meta:
        db_table = "Adresses"
        verbose_name = "Adress"

    def __str__(self):
        return "Улица: " + self.street + " Дом: " + self.build + " Квартира: " + self.flat