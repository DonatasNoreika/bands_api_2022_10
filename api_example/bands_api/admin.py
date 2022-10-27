from django.contrib import admin
from .models import (Band,
                     Song,
                     Album,
                     AlbumReview,
                     AlbumReviewLike)

# Register your models here.

class BandAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Band, BandAdmin)
admin.site.register(Song)
admin.site.register(Album)
admin.site.register(AlbumReview)
admin.site.register(AlbumReviewLike)