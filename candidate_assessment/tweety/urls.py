from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'tweet-word-clouds', views.TweetWordCloudAPIViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.HelloAPIView.as_view()),
    path('api/', include(router.urls)),
    path('register/', views.UserRegisterAPIView.as_view()),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
