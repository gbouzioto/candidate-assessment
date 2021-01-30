import uuid

from django.db import models


class TweetWordCloud(models.Model):
    """ Represents a TweetWordCloud entity """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_tweet_timestamp = models.DateTimeField(null=True, db_index=True)
    last_tweet_timestamp = models.DateTimeField(null=True, db_index=True)
    topic = models.CharField(max_length=255)
    words = models.TextField(help_text="comma separated words from tweeter given a specific hashtag and a timespan")

    def __str__(self):
        return self.id
