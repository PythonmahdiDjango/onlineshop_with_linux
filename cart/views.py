from django.shortcuts import render, get_object_or_404, redirect

from products.models import Product
from .cart import Cart
from .forms import AddToCartProductForm


def cart_detail_view(request):

    """ show products in the cart for payment """

    cart = Cart(request)
    
    return render(request, "cart/cart_detail.html", {
        "cart": cart,
    })


def add_to_cart_view(request, product_id):

    """ get product and its quantity from request.POST and add it to
    cart then redirect to cart_detail """

    cart = Cart(request)

    product = get_object_or_404(Product, id=product_id)

    form = AddToCartProductForm(request.POST)

    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data["quantity"]

        cart.add(product, quantity)
    
    return redirect("cart:cart_detail")


def remove_from_cart(request, product_id):

    """ remove a product from the cart """

    cart = Cart(request)

    product = get_object_or_404(Product, id=product_id)
    
    cart.remove(product)

    return redirect("cart:cart_detail")
