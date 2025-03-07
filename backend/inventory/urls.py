from django.urls import path
from .controller import product_controller

urlpatterns = [
    path('get-products', product_controller.get_products, name='get-products')
]