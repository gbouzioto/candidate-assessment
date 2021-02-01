"""tweety urls"""
from django.urls import include, path
from rest_framework.authtoken import views as auth_token_views

from . import views

urlpatterns = [
    path('', views.HelloAPIView.as_view()),
    path('api/tweet-word-cloud/', views.TweetWordCloudAPIView.as_view()),
    path('api/register/', views.UserRegisterAPIView.as_view()),
    path('api/token-auth/', auth_token_views.obtain_auth_token),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]
