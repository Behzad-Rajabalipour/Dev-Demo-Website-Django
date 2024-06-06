# Generated by Django 4.1.5 on 2023-02-08 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_alter_brand_image_name_alter_product_image_name_and_more'),
        ('discount', '0003_alter_discountbasketdetail_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discountbasketdetail',
            name='discount_basket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discountBasket_details', to='discount.discountbasket'),
        ),
        migrations.AlterField(
            model_name='discountbasketdetail',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_discountDetails', to='products.product'),
        ),
    ]