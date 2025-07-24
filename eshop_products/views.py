import itertools
from django.views.generic import ListView
from django.http.response import Http404
from django.shortcuts import render

from .models import Products, ProductsGallery
from eshop_products_categories.models import ProductsCategories
from eshop_cart.forms import AddToCartForm


class ProductsList(ListView):
    template_name = 'products\prodcut_list.html'
    paginate_by = 4

    def get_queryset(self):
        return Products.objects.get_active_products()


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def products_details(request, *args, **kwargs):
    pk = kwargs['pk']
    product = Products.objects.get_by_id(pk)
    if product is None:
        raise Http404

    add_to_cart = AddToCartForm(initial={'product_id': pk})

    product_gallery = ProductsGallery.objects.filter(products_id=pk)
    products_list_galleries = list(my_grouper(3, product_gallery))

    products_related = Products.objects.get_related_products(
        product=product, pk=pk)
    products_list_related = list(my_grouper(3, products_related))

    context = {
        'product': product,
        'products_galleries': products_list_galleries,
        'products_list_related': products_list_related,
        'add_to_cart': add_to_cart,
    }
    return render(request, 'products\product_details.html', context)


class SearchProducts(ListView):
    template_name = 'products\prodcut_list.html'
    paginate_by = 12

    def get_queryset(self):
        query = self.request.GET.get('sr')
        if query is not None:
            return Products.objects.search(query)
        return Products.objects.none()


class ProductsListByCategories(ListView):
    template_name = 'products\prodcut_list.html'
    paginate_by = 12

    def get_queryset(self):
        category__name = self.kwargs['category_name']
        category = ProductsCategories.objects.filter(
            name__iexact=category__name).first()
        
        
        if category is None:
            raise Http404

        return Products.objects.get_by_category(category__name)


def categories_list_partial(request, *args, **kwargs):
    categories = ProductsCategories.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'products\categories_list_partial.html', context)
