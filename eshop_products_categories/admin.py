from django.contrib import admin
from django.contrib.admin.decorators import display

from .models import ProductsCategories
# Register your models here.


class ProductsCategoriesAdmin(admin.ModelAdmin):
    list_display = ['title', 'name']

    class Meta:
        model = ProductsCategories

admin.site.register(ProductsCategories, ProductsCategoriesAdmin)
