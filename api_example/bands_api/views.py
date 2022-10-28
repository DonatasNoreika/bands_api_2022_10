from django.shortcuts import render
from rest_framework import generics, permissions
from .models import (Band,
                    Album,
                    AlbumReview)
from .serializers import (BandSerializer,
                          AlbumReviewSerializer,
                          AlbumSerializer,
                          AlbumAlbumReviewSerializer)
from rest_framework.exceptions import ValidationError

# Create your views here.
class BandListAPI(generics.ListCreateAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BandDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AlbumListAPI(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AlbumDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AlbumReviewListAPI(generics.ListCreateAPIView):
    queryset = AlbumReview.objects.all()
    serializer_class = AlbumReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AlbumAlbumReviewListAPI(generics.ListCreateAPIView):
    # queryset = AlbumReview.objects.all()
    serializer_class = AlbumAlbumReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        album = Album.objects.get(pk=self.kwargs['pk'])
        return AlbumReview.objects.filter(album=album)

    def perform_create(self, serializer):
        album = Album.objects.get(pk=self.kwargs['pk'])
        serializer.save(user=self.request.user, album=album)

class AlbumReviewDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = AlbumReview.objects.all()
    serializer_class = AlbumReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        albumreview = AlbumReview.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if albumreview.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError('Negalima trinti svetimų albumų apžvalgų!')

    def put(self, request, *args, **kwargs):
        albumreview = AlbumReview.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if albumreview.exists():
            return self.update(request, *args, **kwargs)
        else:
            raise ValidationError('Negalima koreguoti svetimų albumų apžvalgų!')