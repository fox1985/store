from django.db import models
from users.models import User
# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='Имя категории')
    description = models.TextField(blank=True, verbose_name='Описания категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=256,verbose_name='Имя товара')
    image = models.ImageField(upload_to='products_images', blank=True, verbose_name='Изображение')
    description = models.TextField(blank=True, verbose_name='Описания')
    short_description = models.CharField(max_length=64, blank=True, verbose_name='Краткое Описания')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE,verbose_name='Категория')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveIntegerField(default=0, verbose_name='подщет')
    created_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Карзина'
        verbose_name_plural = 'Карзина'

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'

    def sum(self):
        return self.quantity * self.product.price