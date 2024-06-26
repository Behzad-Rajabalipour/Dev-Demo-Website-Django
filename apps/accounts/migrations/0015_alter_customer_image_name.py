# Generated by Django 4.1.5 on 2023-02-08 15:44

from django.db import migrations, models
import utils


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_alter_customer_image_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='image_name',
            field=models.ImageField(blank=True, null=True, upload_to=utils.FileUpload.upload_to),
        ),
    ]
