from rest_framework import serializers
from .models import ProductCategory

class CategorySerializer(serializers.ModelSerializer):
      class Meta:
          model=ProductCategory
          fields=('id', 'name', 'parent')
          read_only_fields=('created_at', 'updated_at', 'updated_by')
