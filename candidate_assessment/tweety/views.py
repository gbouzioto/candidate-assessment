"""
tweety Views
"""
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
    """
    Endpoint for viewing tweet-word clouds.
    Requires TokenAuthentication
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        """
        Post request to api/tweet-word-cloud/ endpoint.
        Requires the arguments 'response_format', 'words'.

        :param request: an api request
        :param args: request args
        :param kwargs: request args
        :returns: A Response object with content a dictionary returned
        from utils.TweetTextParser.extract_word_cloud method.
        :raises: serializers.ValidationError | exceptions.TweetyParserException |
        exceptions.TweetyGeneralException
        """
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
        except Exception as err:
            details = "Error creating daily word cloud. Contact support for more info."
            logger.exception(err)
            raise exceptions.TweetyGeneralException(detail=details)


class UserRegisterAPIView(generics.CreateAPIView):
    """ User Registration API Endpoint """
    queryset = User.objects.all()
    serializer_class = serializers.UserRegistrationSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        """
        Post request to api/register/ endpoint.
        Requires the arguments "username", "password".

        :param request: an api request
        :param args: request args
        :param kwargs: request args
        :returns: A Response object with the following content:
        {
            'success': 'True',
            'status code': status.HTTP_200_OK,
            'message': 'User registered  successfully',
        }
        :raises: serializers.ValidationError
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_200_OK
        message = f"User: {serializer.data['username']} registered successfully."
        content = {
            'success': 'True',
            'status code': status_code,
            'message': message,
        }
        logger.info(message)
        return Response(content, status=status_code)


class HelloAPIView(views.APIView):
    """
    Hello API Endpoint
    Requires TokenAuthentication
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        Welcoming get request.
        :param request: an api request
        :param args: request args
        :param kwargs: request args
        :returns: A Response object with a simple message
        """
        content = {"message": "Hello my name is Tweety!"}
        return Response(content)
