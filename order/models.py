from django.conf import settings
from django.db import models
from cart.models import Cart
from shop.models import Product
from django.utils import timezone

# Create your models here.
ORDER_STATUS_CHOICES = (
    ('Принять в обработку', 'Принять в обработку'),
    ('Выполняется', 'Выполняется'),
    ('Оплачен', 'Оплачен')
)


class Order(models.Model):                            # оформление заказа     № заказа
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=False)
    items = models.ForeignKey(Cart, on_delete=models.CASCADE, default=1)
    total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=300, blank=True)
    buying_type = models.CharField(max_length=40, choices=(('Самовывоз', 'Самовывоз'), ('Доставка', 'Доставка')), default='Самовывоз')
    date = models.DateTimeField(auto_now_add=True)
    comments = models.TextField()
    status = models.CharField(max_length=100, choices=ORDER_STATUS_CHOICES, default=True)

    def __str__(self):
        return 'Заказ №{0}'.format(str(self.id))
