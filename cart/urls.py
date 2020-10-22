from django.urls import path,include
from .views import view_cart

app_name = 'cart'
urlpatterns = [
    path('view/', view_cart, name="view"),
    ]
