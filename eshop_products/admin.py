from django.contrib import admin

from .models import Products, ProductsGallery
# Register your models here.


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'tittle', 'price', 'is_active']

    class Meta:
        model = Products


class ProductsGalleryAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'image', 'products']

    class Meta:
        model = Products


admin.site.register(Products, ProductsAdmin)
admin.site.register(ProductsGallery, ProductsGalleryAdmin)
