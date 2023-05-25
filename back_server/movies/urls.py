from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('all_movies/', views.all_movies),
    path('recommends/<int:page>/', views.recommend_list),
    path('latest_release/<int:page>/', views.latest_release),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/like/', views.like_movie),
    path('<int:movie_pk>/reviews/create/', views.create_review),
    path('reviews/<int:review_pk>/', views.manage_review),
    path('collections/', views.collection_list),
    path('collections/<int:collection_id>/', views.collection_detail),
    path('otts/', views.get_otts),
    path('otts/<int:ott_id>/', views.movies_by_ott),
]