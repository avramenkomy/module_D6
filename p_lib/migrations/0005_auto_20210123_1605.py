# Generated by Django 3.1.5 on 2021-01-23 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_lib', '0004_auto_20210123_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='birth_year',
            field=models.SmallIntegerField(verbose_name='Год рождения'),
        ),
        migrations.AlterField(
            model_name='author',
            name='country',
            field=models.CharField(max_length=255, verbose_name='Страна'),
        ),
    ]
