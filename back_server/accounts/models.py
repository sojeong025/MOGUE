from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    nickname = models.CharField(max_length=15, blank=False, null=False)
    followings = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followers')
    profile_img = models.ImageField(null=True, blank=True, upload_to='profile_imgs/', default="default.jpg")