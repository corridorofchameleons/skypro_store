# Generated by Django 5.0.4 on 2024-05-21 17:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('slug', models.CharField(max_length=110, verbose_name='Slug')),
                ('content', models.TextField(verbose_name='Содержимое')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='Изображение')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 5, 21, 17, 54, 56, 291583), verbose_name='Дата создания')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')),
            ],
        ),
    ]
