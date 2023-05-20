from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=254)
    profile_img = serializers.ImageField(required=False, allow_empty_file=True)

    class Meta:
        model = User
        fields = '__all__'