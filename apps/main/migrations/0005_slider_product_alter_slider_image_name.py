# Generated by Django 4.1.5 on 2024-01-03 15:14

from django.db import migrations, models
import django.db.models.deletion
import utils


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0040_alter_brand_image_name_alter_product_image_name_and_more'),
        ('main', '0004_alter_slider_image_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='product',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='slider', to='products.product'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='image_name',
            field=models.ImageField(upload_to=utils.FileUpload.upload_to),
        ),
    ]
