from rest_framework import status
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from .models import Product
from .serializers import ProductSerializer
import logging

logger = logging.getLogger(__name__)


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

    
    def product_list(request):
        logger.error(request.method)
        if request.method == 'GET':
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            return JSONResponse(serializer.data)

        if request.method=='POST':
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data, status=status.HTTP_201_CREATED)
            return JSONResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)