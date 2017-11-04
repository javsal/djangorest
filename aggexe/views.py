from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Avg, Max, FloatField, Count

from .models import Author, Publisher, Book, Store
from .serializers import AuthorSerializer, PublisherSerializer, BookSerializer

@api_view(['GET'])
def agg_query(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        # books = Book.objects.count()
        # books = Book.objects.all().aggregate(Avg('price'))
        # books = Book.objects.all().aggregate(Max('price'))
        # books=Book.objects.aggregate(price_diff=Max('price', output_field=FloatField()) - Avg('price'))
        pubs = Publisher.objects.annotate(num_books=Count('book'))
        # serializer = BookSerializer(books, many=True)
        return Response(pubs)
