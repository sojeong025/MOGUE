from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import EditorArticle, UserArticle, Comment
from .serializers import EditorArticleSerializer, UserArticleSerializer, CommentSerializer
from random import sample


# EDITOR ARTICLE
@api_view(['GET'])
@permission_classes([AllowAny])
def editor_articles(request):
    editor_articles = get_list_or_404(EditorArticle)
    # editor_articles = sample(editor_articles, 5)

    serializer = EditorArticleSerializer(editor_articles, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_random_editor_articles(request):
    count = int(request.GET.get('count')) 
    total_articles = EditorArticle.objects.count()
    count = min(count, total_articles)
    random_ids = sample(range(1, total_articles + 1), count)
    random_ids = list(set(random_ids))  # 중복 제거
    random_articles = EditorArticle.objects.filter(id__in=random_ids)
    serializer = EditorArticleSerializer(random_articles, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def editor_article_detail(request, editor_article_pk):
    editor_article = get_object_or_404(EditorArticle, pk=editor_article_pk)

    serializer = EditorArticleSerializer(editor_article)

    return Response(serializer.data, status=status.HTTP_200_OK)


#USER_ARTICLE
@api_view(['GET'])
@permission_classes([AllowAny])
def user_articles(request, page):
    user_articles = UserArticle.objects.all()
    user_articles = user_articles[page:page+5]
    serializer = UserArticleSerializer(user_articles, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

#USER_ARTICLE
@api_view(['GET'])
@permission_classes([AllowAny])
def user_articles_length(request):
    user_articles = UserArticle.objects.all()
    serializer = UserArticleSerializer(user_articles, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def user_article_detail(request, user_article_pk):
    user_article = get_object_or_404(UserArticle, pk=user_article_pk)
    comments = Comment.objects.filter(article_id=user_article_pk)
    user_article_serializer = UserArticleSerializer(user_article)
    comments_serializer = CommentSerializer(comments, many=True)    
    context = {
        'user_article': user_article_serializer.data,
        'comments': comments_serializer.data,
    }
    return Response(context, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def create_user_article(request):
    serializer = UserArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def manage_user_article(request, user_article_pk):
    user_article = get_object_or_404(UserArticle, pk=user_article_pk)
    if request.user.id == user_article.user_id:
        if request.method == 'PUT':
            serializer = UserArticleSerializer(instance=user_article, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            
        elif request.method == 'DELETE':
            user_article.delete()
            return Response("삭제되었습니다.", status=status.HTTP_204_NO_CONTENT)
    else:
        return Response("권한이 없습니다", status=status.HTTP_403_FORBIDDEN)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_comments(request):
    comments = Comment.objects.all().filter(user=request.user)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def create_comment(request, user_article_pk):
    user_article = UserArticle.objects.get(id=user_article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, article=user_article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def manage_comment(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.user == comment.user:
        if request.method == 'PUT':
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        
        elif request.method == 'DELETE':
            comment.delete()
            return Response('삭제되었습니다', status=status.HTTP_204_NO_CONTENT)
        
    else:
        return Response('권한이 없습니다', status=status.HTTP_403_FORBIDDEN)