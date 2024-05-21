from django.db import models
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=110, verbose_name='Slug')
    content = models.TextField(verbose_name='Содержимое')
    image = models.ImageField(upload_to='blog/', verbose_name='Изображение', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', default=timezone.now())
    is_published = models.BooleanField(verbose_name='Опубликовано', default=True)
    views = models.PositiveIntegerField(verbose_name='Количество просмотров', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
