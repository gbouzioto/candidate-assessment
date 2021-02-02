"""tweety urls"""
from django.urls import path
from rest_framework.authtoken import views as auth_token_views

from . import views

app_name = 'tweety-api'

urlpatterns = [
    path('', views.HelloAPIView.as_view(), name="home"),
    path('tweet-word-cloud/', views.TweetWordCloudAPIView.as_view(), name="tweet-word-cloud"),
    path('register/', views.UserRegisterAPIView.as_view(), name='register'),
    path('token-auth/', auth_token_views.obtain_auth_token, name='token-auth')
]
