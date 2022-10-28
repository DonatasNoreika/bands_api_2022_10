from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Band(models.Model):
    name = models.CharField(verbose_name='Name', max_length=200)

    def __str__(self):
        return f"Band {self.name}"


class Album(models.Model):
    name = models.CharField(verbose_name='Name', max_length=200)
    band = models.ForeignKey(to="Band", on_delete=models.CASCADE)

    def __str__(self):
        return f"Album {self.name} of band {self.band.name}"


class Song(models.Model):
    name = models.CharField(verbose_name='Name', max_length=200)
    duration = models.DurationField(verbose_name="Duration")
    album = models.ForeignKey(to="Album", on_delete=models.CASCADE)

    def __str__(self):
        return f"Song {self.name} of album {self.album.name}"


class AlbumReview(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    album = models.ForeignKey(to="Album", on_delete=models.CASCADE, related_name='reviews')
    content = models.TextField(verbose_name="Content", max_length=3000, null=True, blank=True)
    score = models.IntegerField(verbose_name="Score")

    def __str__(self):
        return f"Album {self.album.name} of album {self.album.band.name} review"


class AlbumReviewLike(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    album_review = models.ForeignKey(to=AlbumReview, on_delete=models.CASCADE)

    def __str__(self):
        return f"User {self.user} like of {self.album_review.id} review"
