# Generated by Django 4.1.5 on 2024-01-01 02:29

from django.db import migrations, models
import utils


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_slider_image_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='image_name',
            field=models.ImageField(upload_to=utils.FileUpload.upload_to),
        ),
    ]
