# Generated by Django 4.1.5 on 2024-01-01 02:01

from django.db import migrations, models
import utils


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0036_alter_brand_image_name_alter_product_image_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='image_name',
            field=models.ImageField(upload_to=utils.FileUpload.upload_to, verbose_name='Brand Image Name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_name',
            field=models.ImageField(upload_to=utils.FileUpload.upload_to, verbose_name='Product Image Name'),
        ),
        migrations.AlterField(
            model_name='productgallery',
            name='image_name',
            field=models.ImageField(upload_to=utils.FileUpload.upload_to),
        ),
        migrations.AlterField(
            model_name='productgroup',
            name='image_name',
            field=models.ImageField(upload_to=utils.FileUpload.upload_to, verbose_name='ProductGroup Image Name'),
        ),
    ]
