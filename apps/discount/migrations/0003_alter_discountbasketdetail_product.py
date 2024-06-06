# Generated by Django 4.1.5 on 2023-02-08 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_alter_brand_image_name_alter_product_image_name_and_more'),
        ('discount', '0002_alter_coupon_discount_alter_discountbasket_discount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discountbasketdetail',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='product_discountDetails'),
        ),
    ]