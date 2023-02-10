from django.db import models


class Product(models.Model):
    SIZE = (
        ('1', 'S'),
        ('2', 'M'),
        ('3', 'L'),
        ('4', 'XL'),
        ('5', 'XXL'),
    )
    name = models.CharField(max_length=20, verbose_name='Название продукта')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    discription = models.CharField(max_length=200, verbose_name='Описание')
    color = models.CharField(max_length=20, verbose_name='Цвет')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural ='Продукты'

    def __str__(self) -> str:
        return self.name

class Order(models.Model):
    name = models.CharField(max_length=20,verbose_name='Название')
    phone_num = models.CharField(max_length=20,verbose_name='Номер телефона')
    adress = models.CharField(max_length=50, verbose_name='Адрес')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self) -> str:
        return self.name

    




