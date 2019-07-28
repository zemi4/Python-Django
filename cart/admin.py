from django.contrib import admin

from cart.models import Cart
from . import models

# Register your models here.
admin.site.register(models.CartItem)


class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'cart_total']


admin.site.register(Cart, CartAdmin)