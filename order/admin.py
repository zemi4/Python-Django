from django.contrib import admin
from .models import Order
from . import models


# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'total', 'first_name', 'last_name', 'phone', 'address', 'date', 'comments', 'status']
    list_editable = ['status']


admin.site.register(Order, OrderAdmin)