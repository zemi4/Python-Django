# Generated by Django 2.2.3 on 2019-07-27 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='product_title',
            field=models.CharField(default='DELL', max_length=120),
        ),
    ]
