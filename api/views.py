from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import PlayerListSerializer, DistrictListSerializer
from .models import PlayerList, DistrictList

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = PlayerList.objects.all()
    serializer_class = PlayerListSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = PlayerList.objects.all()
    serializer_class = PlayerListSerializer


class CreateDistrictView(generics.ListCreateAPIView):
    queryset=DistrictList.objects.all()
    serializer_class=DistrictListSerializer

    def perform_create(self, serializer):
            serializer.save()