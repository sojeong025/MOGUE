from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# class WatchProviders(models.Model):
#     logo_path = models.TextField()
#     provider_name = models.CharField(max_length=50)

class User(AbstractUser):
    first_name = None
    last_name = None
    email = models.EmailField(max_length=254)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)
    nickname = models.CharField(max_length=50)
    profile_img = models.ImageField(null=True, blank=True, upload_to='profile_imgs/')