from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class ProductSerializer(serializers.ModelSerializer):
    # category=CategorySerializer(required=False) # To view detail of foreign key feild
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'uom', 'category')
