from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from core.api import api_add_to_cart
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls'), name="core"),
    path('cart/', include('cart.urls'), name="cart"),
    path('api/add_to_cart/',api_add_to_cart,name='api_add_to_cart'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
