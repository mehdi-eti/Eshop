from django.urls import path

from .views import (ProductsList,
                    products_details,
                    SearchProducts,
                    ProductsListByCategories,
                    categories_list_partial,
                    )

urlpatterns = [
    path('', ProductsList.as_view(), name='products'),

    path('<int:pk>/<str:tittle>', products_details, name='products-details'),

    path('search', SearchProducts.as_view(), name='products-search'),

    path('<str:category_name>',
         ProductsListByCategories.as_view(),
         name='category_name'),
         
    path('categories_list_partial/',
         categories_list_partial,
         name='categories_list_partial')
]
