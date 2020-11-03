from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Product
from cart.cart import Cart
import json


def api_add_to_cart(request):
    data = json.loads(request.body)
    jsonresponse = {'success': True}
    product_id = data['product_id']
    update = data['update']
    quantity = data['quantity']

    cart = Cart(request)
    print(update)
    #print(data)
    product = get_object_or_404(Product, pk=product_id)

    if not update:
        cart.add(product=product, quantity=1, update_quantity=False)
    else:
        cart.add(product=product, quantity=1)
    return JsonResponse(jsonresponse)


def api_remove_from_cart(request):
    data = json.loads(request.body)
    jsonresponse = {'success': True}

    cart = Cart(request)
    cart.remove(data['product_id'][0][0])
    return JsonResponse(jsonresponse)
