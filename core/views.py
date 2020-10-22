from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product


def landingpage(request):
    return render(request, 'home.html', {})


class ProductDetailView(DetailView):
    model = Product

    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Product, slug=kwargs['slug'])
        context = {'product': product}
        return render(request,'core/product_detail.html',context)


class ProductListView(ListView):
    model = Product

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        context = {'products': products}
        return render(request,'core/product_list.html', context)
