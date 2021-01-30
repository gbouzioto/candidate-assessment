from django.contrib.auth.models import User
from rest_framework import serializers

from .models import TweetWordCloud


class TweetWordCloudSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer class for model TweetWordCloud """
    class Meta:
        model = TweetWordCloud
        fields = ["url", "first_tweet_timestamp", "last_tweet_timestamp", "topic", "words"]


class UserRegistrationSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer class for model User """
    class Meta:
        model = User
        fields = ["url", "username", "password"]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """ Creates a User entity and stores it into the db """
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
