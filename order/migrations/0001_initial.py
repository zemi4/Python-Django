# Generated by Django 2.2.3 on 2019-07-27 10:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('phone', models.CharField(max_length=50)),
                ('address', models.CharField(blank=True, max_length=300)),
                ('buying_type', models.CharField(choices=[('Самовывоз', 'Самовывоз'), ('Доставка', 'Доставка')], default='Самовывоз', max_length=40)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('comments', models.TextField()),
                ('status', models.CharField(choices=[('Принять в обработку', 'Принять в обработку'), ('Выполняется', 'Выполняется'), ('Оплачен', 'Оплачен')], default=True, max_length=100)),
                ('items', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cart.Cart')),
                ('user', models.ForeignKey(default='Sasha', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
