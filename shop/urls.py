from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('category/<str:category_slug>/', views.category_view, name='category_detail'),
    path('product/<str:product_slug>', views.product_view, name='product_detail'),
]
