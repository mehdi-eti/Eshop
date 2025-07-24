from django.contrib import admin

from .models import Cart, CartDetail
# Register your models here.


class CartAdmin(admin.ModelAdmin):
    list_display = ['owner', 'is_paid', 'payment_date']
    list_editable = ['is_paid']
    search_fields = ['owner']
    list_filter = ['is_paid']


admin.site.register(Cart, CartAdmin)


class CartDetailAdmin(admin.ModelAdmin):
    list_display = ['cart', 'product', 'price', 'count']
    search_fields = ['cart', 'product']


admin.site.register(CartDetail, CartDetailAdmin)
