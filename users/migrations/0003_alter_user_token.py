# Generated by Django 5.0.4 on 2024-06-11 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(default='', max_length=100, verbose_name='Токен'),
        ),
    ]
