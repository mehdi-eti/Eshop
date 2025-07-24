import itertools
from django.shortcuts import render

from esho_slider.models import Sliders
from eshop_settings.models import Settings
from eshop_products.models import Products


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


# TODO: """ Header View """
def header(request, *args, **kwargs):
    context = {

    }
    return render(request, 'share/header.html', context)


# TODO: """ Core View """
def coreView(request):
    slider: Sliders = Sliders.objects.filter(is_active=True)
    most_views: Products = Products.objects.order_by('-count_visit').all()[:8]
    most_views_list = list(my_grouper(4, most_views))
    newest: Products = Products.objects.all()[:8]
    newestes_list = list(my_grouper(4, newest))
    context = {
        'sliders': slider,
        'most_views_list': most_views_list,
        'newestes_list': newestes_list,
    }
    return render(request, 'index.html', context)


# TODO: """ Footer View """
def footer(request, *args, **kwargs):
    setting = Settings.objects.first()
    context = {
        'aboutUs': setting
    }
    return render(request, 'share/footer.html', context)
