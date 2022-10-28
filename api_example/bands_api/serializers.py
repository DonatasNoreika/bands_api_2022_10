from rest_framework import serializers

from .models import (Band,
                    Album,
                    AlbumReview)

class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = ['id', 'name']

class MyAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'name', 'band']


class AlbumReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    album = MyAlbumSerializer()

    class Meta:
        model = AlbumReview
        fields = ['id', 'user', 'user_id', 'album', 'content', 'score']


class AlbumAlbumReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    album = serializers.ReadOnlyField(source='album.id')

    class Meta:
        model = AlbumReview
        fields = ['id', 'user', 'user_id', 'album', 'content', 'score']

class AlbumSerializer(serializers.ModelSerializer):
    reviews = AlbumReviewSerializer(many=True)
    reviews_count = serializers.SerializerMethodField()

    class Meta:
        model = Album
        fields = ['id', 'name', 'band', 'reviews', 'reviews_count']

    def get_reviews_count(self, obj):
        return AlbumReview.objects.filter(album=obj).count()