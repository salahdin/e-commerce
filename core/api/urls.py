from .serializers import ProductSerializer
from django.urls import path, include
from rest_framework import routers
from .import views

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]