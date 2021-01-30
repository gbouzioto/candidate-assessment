from django.contrib.auth.models import User
from rest_framework import viewsets, generics, views, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .models import TweetWordCloud
from .serializers import TweetWordCloudSerializer, UserRegistrationSerializer


class TweetWordCloudAPIViewSet(viewsets.ReadOnlyModelViewSet):
    """ Endpoint for viewing tweet-word clouds """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    serializer_class = TweetWordCloudSerializer
    permission_classes = [IsAuthenticated]
    queryset = TweetWordCloud.objects.all().order_by('-first_tweet_timestamp')


class UserRegisterAPIView(generics.CreateAPIView):
    """ User Registration API Endpoint """
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success': 'True',
            'status code': status.HTTP_200_OK,
            'message': 'User registered  successfully',
        }
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)


class HelloAPIView(views.APIView):
    """ Hello API Endpoint """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {"message": "Hello my name is Tweety!"}
        return Response(content)

