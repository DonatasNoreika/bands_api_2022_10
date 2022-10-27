from django.shortcuts import render
from rest_framework import generics, permissions
from .models import (Band,
                    AlbumReview)
from .serializers import (BandSerializer,
                        AlbumReviewSerializer)

# Create your views here.
class BandListAPI(generics.ListCreateAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BandDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AlbumReviewListAPI(generics.ListCreateAPIView):
    queryset = AlbumReview.objects.all()
    serializer_class = AlbumReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


