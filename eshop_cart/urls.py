from django.urls import path

from .views import add_cart_view, open_cart, remove_item

urlpatterns = [
    path('', open_cart, name='open_cart'),
    path('add-cart', add_cart_view, name='add_cart_view'),
    path('remove-item/<int:pk>', remove_item, name='remove-item'),
]
