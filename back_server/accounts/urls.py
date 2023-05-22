from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', obtain_jwt_token),
    # path('profile/', views.profile),
    path('profile/<int:user_pk>/', views.profile),
    path('delete/', views.user_delete),
    path('<int:user_pk>/follow/', views.follow),
    path('<int:user_pk>/follow_list/', views.follow_list),
    path('change_password/<int:user_pk>/', views.change_password),
    # path('favorite/<int:user_pk>/', views.favorite_list),
]