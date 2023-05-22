from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('all_movies/', views.all_movies),
    path('recommends/<int:page>/', views.recommend_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/reviews/create/', views.create_review),
    path('<int:movie_pk>/reviews/<int:review_pk>/', views.manage_review),
    path('collections/', views.collection_list),
    path('collections/<int:collection_id>/', views.collection_detail)
]