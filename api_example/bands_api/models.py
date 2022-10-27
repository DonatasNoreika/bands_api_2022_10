from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Band(models.Model):
    name = models.CharField(verbose_name='Name', max_length=200)


class Album(models.Model):
    name = models.CharField(verbose_name='Name', max_length=200)
    band = models.ForeignKey(to="Band", on_delete=models.CASCADE)


class Song(models.Model):
    name = models.CharField(verbose_name='Name', max_length=200)
    duration = models.DurationField(verbose_name="Duration")
    album = models.ForeignKey(to="Album", on_delete=models.CASCADE)


class AlbumReview(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    album = models.ForeignKey(to="Album", on_delete=models.CASCADE)
    content = models.TextField(verbose_name="Content", max_length=3000, null=True, blank=True)
    score = models.IntegerField(verbose_name="Score")


class AlbumReviewLike(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    album_review = models.ForeignKey(to=AlbumReview, on_delete=models.CASCADE)
