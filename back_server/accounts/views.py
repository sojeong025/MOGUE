from django.http.response import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from rest_framework import serializers, status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.contrib.auth import get_user_model, update_session_auth_hash
from .models import User
from .serializers import UserSerializer
from movies.models import Movie, Review
# from movies.serializers import MovieSerializer, ReviewSerializer
from community.models import Community, Ceview
# from community.serializers import CommunitySerializer, CeviewSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
	# 1-1. Client에서 온 데이터를 받아서
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
    nickname = request.data.get('nickname')
	# 1-2. 패스워드 일치 여부 체크
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
	# 2. UserSerializer를 통해 데이터 직렬화
    serializer = UserSerializer(data=request.data)
    serializer.nickname = nickname
	# 3. validation 작업 진행 -> password도 같이 직렬화 진행
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        #4. 비밀번호 해싱 후
        user.set_password(request.data.get('password'))
        user.save()
        # password는 직렬화 과정에는 포함 되지만 → 표현(response)할 때는 나타나지 않는다. (wrtie_only)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
# def profile(request, user_pk):
#     # 유저 정보
#     person = get_object_or_404(User, pk=user_pk)
#     serializer = UserSerializer(person)

#     # 유저가 좋아요 누른 영화
#     likeMoive = Movie.objects.filter(like_users=user_pk)
#     likeserializer = MovieSerializer(likeMoive, many=True)

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

#     # 작성한 게시글
#     community = Community.objects.filter(user=user_pk)
#     comserializer = CommunitySerializer(community, many=True)

#     # 좋아요 누른 게시글
#     likeCommunity = Community.objects.filter(like_users=user_pk)
#     likecomserializer = CommunitySerializer(likeCommunity, many=True)

#     context = {
#         'userInfo': serializer.data,
#         'userLikeMovies': likeserializer.data,
#         'reviewInMovies': reserializer.data,
#         'userCreateCommunity': comserializer.data,
#         'userLikeCommunity': likecomserializer.data,
#         'userFavoriteMovies': favoriteserializer.data,
#     }
#     return Response(context)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def user_delete(request):
    request.user.delete()
    return HttpResponse(status=200)


@api_view(['GET','POST'])
@authentication_classes([JSONWebTokenAuthentication])
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


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def favorite_list(request, user_pk):
#     movies = Movie.objects.filter(favorite_users__in=[user_pk])
#     serializer = MovieSerializer(movies, many=True)
#     user = User.objects.get(pk=user_pk)
#     userserializer = UserSerializer(user)
#     context = {
#         'movies': serializer.data,
#         'user': userserializer.data
#     }
#     return Response(context)