from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import MovieSerializer, ReviewSerializer, CollectionSerializer
from .models import Movie, Review, Collection
# Create your views here.

@api_view(['GET'])
@permission_classes([AllowAny])
def recommend_list(request, page):
    movies = get_list_or_404(Movie)
    movies = sorted(movies, key=lambda x : x.popularity)[page:15+page]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, id=movie_pk)
    print(1)
    reviews = Review.objects.filter(movie_id=movie_pk)
    print(1)
    movie_serializer = MovieSerializer(movie)
    review_serializer = ReviewSerializer(reviews, many=True)
    context = {
        'movie': movie_serializer.data,
        'reviews': review_serializer.data,
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