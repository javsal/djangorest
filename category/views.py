from django.shortcuts import render
from rest_framework import generics
from .serializers import CategorySerializer
from .models import ProductCategory


class ProductCategoryList(generics.ListCreateAPIView):
    
    queryset=ProductCategory.objects.all()
    serializer_class=CategorySerializer

    def perform_create(self, serializer):
        serializer.save()
