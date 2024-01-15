# Generated by Django 4.1.5 on 2023-01-27 15:55

from django.db import migrations, models
import django.db.models.deletion
import utils


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_brand_image_name_alter_product_brand_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='image_name',
            field=models.ImageField(upload_to=utils.FileUpload.upload_to, verbose_name='Brand Image Name'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='product_group',
            field=models.ManyToManyField(related_name='features_of_group', to='products.productgroup', verbose_name='Product Group'),
        ),
        migrations.AlterField(
            model_name='featurevalue',
            name='feature',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feature_values', to='products.feature'),
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
