# Generated by Django 4.1.5 on 2023-02-06 23:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0009_alter_brand_image_name_alter_product_image_name_and_more'),
        ('accounts', '0003_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register_date', models.DateField(default=django.utils.timezone.now)),
                ('update_date', models.DateField(auto_now=True)),
                ('is_finaly', models.BooleanField(default=False)),
                ('order_date', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('discount', models.IntegerField(blank=True, default=None, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_orders', to='accounts.customer')),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'orders',
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveIntegerField(default=1)),
                ('price', models.IntegerField(verbose_name='price of item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_Details', to='orders.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_details', to='products.product')),
            ],
        ),
    ]
