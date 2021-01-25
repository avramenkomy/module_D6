# Generated by Django 3.1.5 on 2021-01-23 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_lib', '0006_auto_20210123_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_author', to='p_lib.author', verbose_name='Автор'),
        ),
    ]
