from rest_framework import serializers
from .models import Author, Publisher, Book, Store


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name')

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ('id', 'name')

class BookSerializer(serializers.ModelSerializer):
    author_count = serializers.IntegerField()
    class Meta:
        model = Book
        fields = ('id', 'name', 'pages', 'price', 'author_count', 'publisher')

class StoreSerializer(serializers.ModelSerializer):
    min_price=serializers.IntegerField()
    max_price=serializers.IntegerField()
    class Meta:
        model = Store
        fields = ('id', 'name', 'books', 'max_price', 'min_price')