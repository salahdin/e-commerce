from django.shortcuts import render
from .cart import Cart


def view_cart(request):
    cart = Cart(request)
    productString = '['
    total = 0
    for i in cart:
        total = i['price'] + total
    for i in cart:
        b = "{'id' : '%s', 'title' : '%s', 'price' : '%s' , 'quantity' : '%s'}," % (i['id'], i['product'].title, i['price'], i['quantity'])
        productString = productString + b
    productString = productString + ']'
    print("length",cart.__len__())
    return render(request, 'cart/cart.html', {'cart': cart, 'total': total, 'productString' : productString})
