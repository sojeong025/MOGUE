from rest_framework import serializers
from .models import EditorArticle, UserArticle, Comment
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.utils.timezone import now
from accounts.serializers import UserSerializer
class EditorArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = EditorArticle
        fields = "__all__"

class UserArticleSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    created_at = serializers.SerializerMethodField()

    def get_created_at(self, obj):
        time_difference = naturaltime(obj.created_at)
        time_difference = time_difference.replace(" ", "")    
        time_difference = time_difference.replace("전", " 전")    
        return time_difference
    class Meta:
        model = UserArticle
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    article = UserArticleSerializer(read_only=True)
    created_at = serializers.SerializerMethodField()

    def get_created_at(self, obj):
        time_difference = naturaltime(obj.created_at)
        time_difference = time_difference.replace(" ", "")    
        time_difference = time_difference.replace("전", " 전")   
        return time_difference
    class Meta:
        model = Comment
        fields = "__all__"