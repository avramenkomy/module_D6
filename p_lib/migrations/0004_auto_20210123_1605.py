# Generated by Django 3.1.5 on 2021-01-23 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_lib', '0003_auto_20210123_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='additional_name',
            field=models.CharField(max_length=255, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=255, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=255, verbose_name='Фамилия'),
        ),
    ]
