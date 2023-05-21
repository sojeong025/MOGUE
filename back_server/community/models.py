from django.db import models
from django.conf import settings
from movies.models import Movie
class EditorArticle(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.TextField()
    rawHTML = models.TextField()


class UserArticle(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_articles', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='user_articles', blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    img = models.ImageField(null=True, blank=True, upload_to='article_image/')
    created_at = models.DateTimeField(auto_now_add=True)
    

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.CASCADE)
    article = models.ForeignKey(UserArticle, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)