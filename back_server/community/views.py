from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import EditorArticle, UserArticle, Comment
from .serializers import EditorArticleSerializer, UserArticleSerializer
from random import sample


@api_view(['GET'])
@permission_classes([AllowAny])
def editor_articles(request):
    editor_articles = get_list_or_404(EditorArticle)
    editor_articles = sample(editor_articles, 15)
    serializer = EditorArticleSerializer(editor_articles, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def editor_article_detail(request, editor_article_pk):
    editor_article = get_object_or_404(EditorArticle, pk=editor_article_pk)
    serializer = EditorArticleSerializer(editor_article)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def user_articles(request):
    user_articles = UserArticle.objects.all()
    serializer = UserArticleSerializer(user_articles, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def user_article_detail(request, user_article_pk):
    user_article = get_object_or_404(UserArticle, pk=user_article_pk)
    comments = Comment
    user_article_serializer = UserArticleSerializer(user_article)
    return Response()

