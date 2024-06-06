# Generated by Django 4.1.5 on 2023-02-24 11:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0026_alter_brand_image_name_alter_product_image_name_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField()),
                ('registerdate', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=False)),
                ('approving_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_approvedComments2', to=settings.AUTH_USER_MODEL, verbose_name='user approved comment')),
                ('comment_parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child_comments', to='comment_scoring_favorites.comment')),
                ('commenting_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comments', to=settings.AUTH_USER_MODEL, verbose_name='user who comment')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_Comments', to='products.product')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
            },
        ),
    ]