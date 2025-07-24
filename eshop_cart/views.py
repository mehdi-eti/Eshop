from django.http.response import Http404
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from eshop_products.models import Products
from .models import Cart, CartDetail
from .forms import AddToCartForm


@login_required(login_url='/login')
def add_cart_view(request):
    add_to_cart = AddToCartForm(request.POST or None)

    if add_to_cart.is_valid():
        order = Cart.objects.filter(
            owner_id=request.user.id, is_paid=False).first()

        if order is None:
            order = Cart.objects.create(owner_id=request.user.id)

        product_id = add_to_cart.cleaned_data.get('product_id')
        count = add_to_cart.cleaned_data.get('count')
        product = Products.objects.get_by_id(product_id)

        order.cartdetail_set.create(
            product_id=product_id, price=product.price, count=count)
        return redirect(f'/products/{product_id}/{product.tittle.replace(" ","-")}')

    return redirect('/products')


@login_required(login_url='/login')
def open_cart(request, *args, **kwargs):
    context = {
        'order': None,
        'details': None
    }

    open_order: Cart = Cart.objects.filter(
        owner_id=request.user.id, is_paid=False).first()

    if open_order is not None:
        context['order'] = open_order
        context['details'] = open_order.cartdetail_set.all()

    return render(request, 'cart\open_cart.html', context)


@login_required(login_url='/login')
def remove_item(request, *args, **kwargs):
    pk = kwargs['pk']

    if pk is not None:
        order_detail = CartDetail.objects.filter(
            product_id=pk, cart__owner_id=request.user.id).first()
        
        if order_detail is not None:
            order_detail.delete()
            return redirect('/carts')
        raise Http404
