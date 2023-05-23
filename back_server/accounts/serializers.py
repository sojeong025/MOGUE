from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'password', 'nickname', 'profile_img')


class UpdateUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = ('nickname', 'profile_img')

class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('pk', 'username', 'nickname', 'profile_img')

class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('pk', 'username', 'nickname', 'profile_img')