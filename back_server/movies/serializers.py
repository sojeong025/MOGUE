from rest_framework import serializers
from .models import Movie, Review, Collection

class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Movie
        fields = ('id', 'title', 'poster_path',)

class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'

class CollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collection
        fields = '__all__'