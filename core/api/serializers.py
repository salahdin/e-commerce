from django.contrib.auth.models import User, Group
from rest_framework import serializers
from ..models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'slug', 'description','price',
                  'date_added', 'image', 'thumbnail',]


