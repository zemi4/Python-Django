# Generated by Django 2.2.3 on 2019-07-27 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cartitem_product_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='product_title',
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='shop.Product'),
        ),
    ]
