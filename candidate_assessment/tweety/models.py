from django.db import models


class Tweet(models.Model):
    """ Represents a Tweet entity """
    timestamp = models.DateTimeField()
    topic = models.CharField
    text = models.TextField()

    def __str__(self):
        return self.id
