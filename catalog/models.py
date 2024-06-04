from django.utils import timezone
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    image = models.ImageField(upload_to='products/', verbose_name='Изображение', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    price = models.FloatField(verbose_name='Цена')
    created_at = models.DateTimeField(verbose_name='Дата создания', default=timezone.now)
    updated_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='versions', verbose_name='Продукт')
    code = models.SmallIntegerField(verbose_name='Номер версии')
    version = models.CharField(max_length=20, verbose_name='Версия')
    current = models.BooleanField(verbose_name='Текущая версия')

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
        unique_together = ('product', 'code')

    def __str__(self):
        return f'{self.code} - {self.version}'


class Contact(models.Model):
    address = models.CharField(max_length=200, verbose_name='Адрес')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(max_length=20, verbose_name='Электронная почта')

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'


