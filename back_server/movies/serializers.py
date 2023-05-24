from rest_framework import serializers
from .models import Movie, Review, Collection, Ott

class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Movie
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'

class CollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collection
        fields = '__all__'

class OttSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ott
        fields = '__all__'