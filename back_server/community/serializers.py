from rest_framework import serializers
from .models import EditorArticle, UserArticle, Comment
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.utils.timezone import now

class EditorArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = EditorArticle
        fields = "__all__"

class UserArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserArticle
        fields = "__all__"
        read_only_fields = ('user',)

class CommentSerializer(serializers.ModelSerializer):

    class Mets:
        model = Comment
        fields = "__all__"