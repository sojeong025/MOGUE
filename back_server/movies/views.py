from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework import status
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import MovieSerializer, ReviewSerializer, CollectionSerializer, OttSerializer
from .models import Movie, Review, Collection, Ott
# Create your views here.

@api_view(['GET'])
@permission_classes([AllowAny])
def recommend_list(request, page):
    movies = get_list_or_404(Movie)
    movies = sorted(movies, key=lambda x : x.popularity, reverse=True)[page:20+page]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def latest_release(request, page):
    movies = get_list_or_404(Movie)
    movies = sorted(movies, key=lambda x : x.release_date, reverse=True)[page:20+page]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def all_movies(request):
    movies = get_list_or_404(Movie)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, id=movie_pk)
    otts = movie.otts.filter(movies=movie_pk)
    reviews = Review.objects.filter(movie_id=movie_pk)
    movie_serializer = MovieSerializer(movie)
    review_serializer = ReviewSerializer(reviews, many=True)
    ott_serializer = OttSerializer(otts, many=True)
    context = {
        'movie': movie_serializer.data,
        'reviews': review_serializer.data,
        'otts': ott_serializer.data
    }
    return Response(context)


@api_view(['GET'])
@permission_classes([AllowAny])
def collection_list(request):
    collections = get_list_or_404(Collection)
    serializer = CollectionSerializer(collections, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def collection_detail(request, collection_id):
    collection = get_object_or_404(Collection, id=collection_id)
    movies = Movie.objects.filter(collection__id=collection_id)

    collection_serializer = CollectionSerializer(collection)
    movie_serializer = MovieSerializer(movies, many=True)

    context = {
        'collection': collection_serializer.data,
        'movies': movie_serializer.data
    }
    
    return Response(context)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_review(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def manage_review(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if request.user == review.user:
        if request.method == 'PUT':
            serializer = ReviewSerializer(review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            
        elif request.method == 'DELETE':
            review.delete()
            return Response('삭제되었습니다', status=status.HTTP_204_NO_CONTENT)
        
    else:
        return Response('권한이 없습니다', status=status.HTTP_403_FORBIDDEN)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    if movie.users.filter(pk=user.pk).exists():
        movie.users.remove(user)
        liked = False
    else:
        movie.users.add(user)
        liked = True
    like_status = {
        'liked': liked
        }
    return JsonResponse(like_status)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_otts(request):
    otts = get_list_or_404(Ott)
    serializer = OttSerializer(otts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def movies_by_ott(request, ott_id):
    ott = get_object_or_404(Ott, pk=ott_id)
    movies = ott.movies.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)