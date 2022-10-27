from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Band
from .serializers import BandSerializer

# Create your views here.
class BandListAPI(generics.ListCreateAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer


class BandDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

