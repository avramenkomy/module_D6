# Generated by Django 3.1.5 on 2021-01-25 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_lib', '0014_auto_20210125_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='small_photo',
            field=models.ImageField(blank=True, default='books_photo\\small\\no_photo_small.jpg', upload_to='books_photo/small'),
        ),
    ]