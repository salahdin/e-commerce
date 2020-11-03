from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view

from ..models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('date_added')
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

