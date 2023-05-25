from django.urls import path
from . import views

app_name = "community"
urlpatterns = [
    path('editor_articles/', views.editor_articles),
    path('editor_articles/<int:editor_article_pk>/', views.editor_article_detail),
    path('editor_articles/random/', views.get_random_editor_articles),
    path('user_articles/', views.user_articles_length),
    path('user_articles/pages/<int:page>/', views.user_articles),
    path('user_articles/create/', views.create_user_article),
    path('user_articles/<int:user_article_pk>/', views.user_article_detail),
    path('user_articles/<int:user_article_pk>/manage/', views.manage_user_article),
    path('user_articles/<int:user_article_pk>/comment/', views.create_comment ),
    path('comment/<int:comment_pk>/', views.manage_comment ),
    path('comment/user_comments/', views.user_comments),
]
