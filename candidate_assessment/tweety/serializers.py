""" tweety Serializers """
from django.contrib.auth.models import User
from rest_framework import serializers


class UserRegistrationSerializer(serializers.ModelSerializer):
    """ Serializer class for model User """
    class Meta:
        """ Meta Class of model User"""
        model = User
        fields = ["username", "password"]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """ Creates a User entity and stores it into the db """
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class TweetWordCloudSerializer(serializers.Serializer):
    """ Serializer class for tweet-word-cloud request"""
    response_format = serializers.ChoiceField(required=True, choices=['json', 'csv'],
                                              help_text="Response format can be either json or csv.")
    words = serializers.IntegerField(required=True, min_value=1,
                                     help_text="Number of words to be returned, must be a positive integer.")
