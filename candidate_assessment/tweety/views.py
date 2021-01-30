import logging

from django.contrib.auth.models import User
from rest_framework import viewsets, generics, views, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from searchtweets import collect_results, gen_request_parameters

from .constants import SEARCH_TWEETS_HASHTAG
from .exceptions import TweetyGeneralException
from .models import TweetWordCloud
from .serializers import TweetWordCloudSerializer, UserRegistrationSerializer
from .utils import search_args

logger = logging.getLogger(__name__)


class TweetWordCloudAPIViewSet(viewsets.ModelViewSet):
    """ Endpoint for viewing tweet-word clouds """
    authentication_classes = [TokenAuthentication]
    serializer_class = TweetWordCloudSerializer
    permission_classes = [IsAuthenticated]
    queryset = TweetWordCloud.objects.all().order_by('-first_tweet_timestamp')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()
        try:
            query = gen_request_parameters(SEARCH_TWEETS_HASHTAG, results_per_call=100)
            tweets = collect_results(query=query,
                                     max_tweets=100,
                                     result_stream_args=search_args)
            content = {"message": "Hello my name is Tweety!"}
        except Exception:
            details = "There was an error while creating the daily word cloud"
            logger.exception(details)
            raise TweetyGeneralException(detail=details)
        return Response(content)


class UserRegisterAPIView(generics.CreateAPIView):
    """ User Registration API Endpoint """
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        content = {
            'success': 'True',
            'status code': status.HTTP_200_OK,
            'message': 'User registered  successfully',
        }
        logger.info(f"User: {serializer} registered successfully")
        status_code = status.HTTP_200_OK
        return Response(content, status=status_code)


class HelloAPIView(views.APIView):
    """ Hello API Endpoint """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        content = {"message": "Hello my name is Tweety!"}
        return Response(content)
