from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('recommends/<int:page>/', views.recommend_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('collections/', views.collection_list),
    path('collections/<int:collection_id>/', views.collection_detail)
]