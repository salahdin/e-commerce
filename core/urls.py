from django.urls import path
from .views import landingpage, ProductDetailView, ProductListView
from .api import api_add_to_cart,api_remove_from_cart

app_name = 'core'
urlpatterns = [
    path('', landingpage, name="home"),
    path('product/<slug:slug>', ProductDetailView.as_view(), name="product_detail"),
    path('products/', ProductListView.as_view(), name="product_list"),
    path('api/api_add_to_cart/',api_add_to_cart,name = 'api_add_to_cart'),
    path('api/api_remove_from_cart/',api_remove_from_cart,name='api_remove_from_cart')
]
