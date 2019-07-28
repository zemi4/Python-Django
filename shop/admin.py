from django.contrib import admin
from .models import Product
from . import models

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['category', 'brand', 'title', 'slug', 'description', 'image', 'price', 'available']
    list_filter = ['category']
    list_editable = ['price', 'available']
    # prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
admin.site.register(models.Category)
admin.site.register(models.Brand)