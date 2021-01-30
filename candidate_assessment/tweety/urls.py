from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views as auth_token_views

from . import views as tweety_views

router = routers.DefaultRouter()
router.register(r'tweet-word-clouds', tweety_views.TweetWordCloudAPIViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', tweety_views.HelloAPIView.as_view()),
    path('api/', include(router.urls)),
    path('register/', tweety_views.UserRegisterAPIView.as_view()),
    path('api-token-auth/', auth_token_views.obtain_auth_token),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
