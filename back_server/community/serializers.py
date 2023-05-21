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
    class Meta:
        model = UserArticle
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):

    class Mets:
        model = Comment
        fields = "__all__"