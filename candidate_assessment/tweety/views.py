import logging

from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import generics, views, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from searchtweets import collect_results, gen_request_parameters

from . import constants as c
from . import exceptions
from . import serializers
from . import utils

logger = logging.getLogger(__name__)


class TweetWordCloudAPIView(views.APIView):
    """ Endpoint for viewing tweet-word clouds """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            serializer = serializers.TweetWordCloudSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            request_format = request.data['response_format']
            words = int(request.data['words'])
            # Twitter API
            query = gen_request_parameters(query=c.TWITTER_QUERY,
                                           start_time=c.ONE_DAY_BEFORE,
                                           end_time=c.ONE_MINUTE_BEFORE,
                                           tweet_fields=c.TWEET_FIELDS,
                                           results_per_call=settings.TWEETS_PER_CALL)
            tweets = collect_results(query=query,
                                     result_stream_args=utils.search_args,
                                     max_tweets=settings.MAX_TWEETS)
            tweet_text_parser = utils.TweetTextParser()
            content = tweet_text_parser.extract_word_cloud(tweets=tweets,
                                                           words=words,
                                                           topic=c.TWITTER_TOPIC,
                                                           fmt=request_format)
            if request_format == 'csv':
                # use the CSV renderer for csv output
                request.accepted_renderer = utils.TweetyCsvRenderer()
            return Response(content)
        except ValidationError:
            raise
        except exceptions.TweetyParserException:
            raise
        except Exception as e:
            details = "Error creating daily word cloud. Contact support for more info."
            logger.exception(e)
            raise exceptions.TweetyGeneralException(detail=details)


class UserRegisterAPIView(generics.CreateAPIView):
    """ User Registration API Endpoint """
    queryset = User.objects.all()
    serializer_class = serializers.UserRegistrationSerializer
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
