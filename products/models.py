from django.db import models
from users.models import User
from django.db.models import Sum


# Create your models here.
# Модели = таблицы


class ProductsCategory(models.Model):
    name = models.CharField(max_length=78, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = ('Product Categories')


    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='products_images', blank=True)
    description = models.TextField(blank=True)
    short_description = models.CharField(max_length=64, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveBigIntegerField(default=0)
    category = models.ForeignKey(ProductsCategory, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.name} | {self.category.name}'


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'Корзина для { self.user.username } | Продукт { self.product.name }'


    def sum(self):
        return self.quantity * self.product.price
