from django.db import models
from django.conf import settings
# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    overview = models.TextField()
    popularity = models.FloatField()
    runtime = models.IntegerField()
    vote_count = models.FloatField()
    poster_path = models.CharField(max_length=200)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_movies')

class Review(models.Model):
    content = models.TextField()
    star = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Collection(models.Model):
    title = models.CharField(max_length=50)
    thumbnail = models.ImageField(null=True, blank=True, upload_to='collection_thumbnails/')
    movies = models.ManyToManyField(Movie, verbose_name='collections')


class Ott(models.Model):
    name = models.CharField(max_length=50)
    logo_path = models.ImageField()
    movies = models.ManyToManyField(Movie, related_name='otts')
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='otts')