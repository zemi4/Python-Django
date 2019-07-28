from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('change_item_qty/', views.change_item_qty, name='change_item_qty'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('order/', views.order_create_view, name='create_order'),
    path('make_order/', views.make_order_view, name='make_order'),
    path('thank_you/', TemplateView.as_view(template_name='order/thank_you.html'), name='thank_you'),
]
