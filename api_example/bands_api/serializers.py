from rest_framework import serializers

from .models import (Band,
                     AlbumReview)

class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = ['id', 'name']


class AlbumReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = AlbumReview
        fields = ['id', 'user', 'user_id', 'album', 'content', 'score']

