from django.http.response import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
from rest_framework import serializers, status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.contrib.auth import get_user_model, update_session_auth_hash
from .models import User
from .serializers import UserSerializer, UpdateUserSerializer
from movies.models import Movie
from movies.serializers import MovieSerializer
from community.models import UserArticle
from community.serializers import UserArticleSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
    nickname = request.data.get('nickname')
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = UserSerializer(data=request.data)
    serializer.nickname = nickname
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request, user_pk):
    # 유저 정보
    user = get_object_or_404(User, pk=user_pk)
    user_serializer = UserSerializer(user)

    followers = user.followers.all()
    followers_serializer = UserSerializer(followers, many=True)

    followings = user.followings.all()
    followings_serializer = UserSerializer(followings, many=True)

    # 유저가 좋아요 누른 영화
    like_moive = user.liked_movies.all()
    likeserializer = MovieSerializer(like_moive, many=True)

#     #찜한 영화
#     movies = Movie.objects.filter(favorite_users__in=[user_pk])
#     favoriteserializer = MovieSerializer(movies, many=True)

#     # 댓글을 단 영화
#     review = Review.objects.filter(user=user_pk)
#     review_li = []
#     for i in range(len(review)):
#         review_li.append(review[i].movie_id)
#     reviewMovie = Movie.objects.filter(id__in=review_li)
#     print(reviewMovie)
#     reserializer = MovieSerializer(reviewMovie, many=True)

    # 작성한 게시글
    articles = UserArticle.objects.filter(user=user_pk)
    articles_serializer = UserArticleSerializer(articles, many=True)

#     # 좋아요 누른 게시글
#     likeCommunity = Community.objects.filter(like_users=user_pk)
#     likecomserializer = CommunitySerializer(likeCommunity, many=True)

    context = {
        'user': user_serializer.data,
        'followers': followers_serializer.data,
        'followings': followings_serializer.data,
        'userLikeMovies': likeserializer.data,
#         'reviewInMovies': reserializer.data,
        'userCreateArticles': articles_serializer.data,
#         'userLikeCommunity': likecomserializer.data,
#         'userFavoriteMovies': favoriteserializer.data,
    }

    return Response(context)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def user_delete(request):
    request.user.delete()
    return HttpResponse(status=200)


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def follow(request, user_pk):
    person = get_object_or_404(User, pk=user_pk)
    user = request.user
    if person != user:
        if person.followers.filter(pk=user.pk).exists():
            person.followers.remove(user)
            follow = True
        else:
            person.followers.add(user)
            follow = False
        follow_status = {
            'follow': follow,
            'followings': person.followings.count(),
            'followers': person.followers.count(),
            }
        return JsonResponse(follow_status)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def follow_list(request, user_pk):
    follower = User.objects.filter(followings__in=[user_pk])
    following = User.objects.filter(followers__in=[user_pk])
    followerserializer = UserSerializer(follower, many=True)
    followingserializer = UserSerializer(following, many=True)
    context = {
        'followers': followerserializer.data,
        'followings': followingserializer.data,
    }
    return Response(context)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request, user_pk):
    old_password = request.data.get('old_password')
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
    if old_password == password:
        return Response({'error': '이전 비밀번호를 다시 사용할 수 없습니다.'}, status=status.HTTP_400_BAD_REQUEST)
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
    
    person = get_object_or_404(User, pk=user_pk)
    serializer = UserSerializer(instance=person, data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        update_session_auth_hash(request, user)
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_profile(request, user_pk):
    original_user = User.objects.get(pk=user_pk)
    print(request.data)
    serializer = UpdateUserSerializer(instance=original_user, data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        update_session_auth_hash(request, user)
        user.save()
        return Response(serializer.data)
    
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_user(request):
    users = User.objects.all()
    serializers = UserSerializer(users, many=True)
    return Response(serializers.data)