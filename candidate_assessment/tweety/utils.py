"""
General utility functions and classes
"""
import datetime
import logging
import re

import searchtweets
from django.conf import settings
from rest_framework_csv.renderers import CSVRenderer

from . import exceptions

logger = logging.getLogger(__name__)

search_args = searchtweets.load_credentials(settings.SEARCH_TWEETS_CREDENTIAL_FILE, env_overwrite=False)


class TweetTextParser(object):
    """Class used for parsing and processing the text attribute of tweets"""
    # REGEX
    LOWER_TEXT_RE = re.compile(r"[a-z]+-?[a-z]+")
    # matches tweeter's cashtags, user_mentions, retweets, urls and numeric words
    NON_WORDS_RE = re.compile(r"([@$][A-Za-z0-9]+)|([^0-9A-Za-z])|(\S*\d+\S*)|(RT)")
    UTC_TIMEZONE_RE = re.compile(r"[TZ]|\.0+")

    def _tokenize_tweet_text(self, text):
        """
        Tokenizes a tweet text using regular expressions
        The regexes are based according to some of the operators from the Twitter API
        https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query
        :returns: A set of the words found within the text
        :rtype: set
        """

        # remove all tabs and newlines
        text = text.replace('\n', '').replace('\t', '')
        # replace all non words with space
        text = re.sub(self.NON_WORDS_RE, " ", text)
        # convert the text to lowercase and tokenize it
        tokens = re.findall(self.LOWER_TEXT_RE, text.lower())
        return set(tokens)

    def _reformat_timezone_str(self, date_string):
        """
        :param date_string: A twitter time zone string
        Example: 2021-01-31T16:07:09.000Z
        :type date_string: str
        :returns: A more user formated string
        Example: 31-01-2021 16:07:09 UTC
        :rtype: str
        """
        if not date_string:
            return ""
        date_string = re.sub(self.UTC_TIMEZONE_RE, " ", date_string).strip()
        return datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S").strftime("%d-%m-%Y %H:%M:%S UTC")

    @staticmethod
    def _extract_first_timestamp(tweets):
        """
        Extracts the first timestamp from tweets
        :param tweets: A list of dictionaries, returned from searchtweets.collect_results function.
        Check methos extract_word_cloud for more details on tweets
        :raises TweetyParserException if no timestamp was found
        :returns: The first timestamp from tweets
        :rtype: str
        """
        for i in range(len(tweets) - 1, -1, -1):
            tweet = tweets[i]
            if created_time := tweet.get('created_at'):
                return created_time
        logger.error("Timestamp not included in tweets.\nConsider adding created_time "
                     "field in the request towards twitter API")
        detail = "Could not retrieve timestamp value from tweets provided by the Twitter API. Please try again later."
        raise exceptions.TweetyParserException(detail=detail)

    def extract_word_cloud(self, tweets, words, topic, fmt='json'):
        """
        Extracts a word cloud up to words for a given tweets iterable.
        The tweets iterable taken from the api is a list of dictionaries
        :param tweets:A list of dictionaries, returned from searchtweets.collect_results function.
        Each one represents a tweet.
        Example:
        {'created_at': '2021-01-31T16:07:19.000Z', 'id': '1355910540359561217',
        'text': '(AP News) Russia arrests over 4,000 at wide protests backing Navalny https://t.co/TkEjlJIX5O
        #Arrests #BlackSea #Business #ChemicalWeapons #COVID-19Pandemic #Crime #DiseasesAndConditions'}

        There are some dictionaries however that are used in order to merged chunks of tweets, which are ignored.
        Example:
        {'newest_id': '1355911626411679745', 'oldest_id': '1355910502237409283', 'result_count': 100,
       'next_token': 'b26v89c19zqg8o3fosktksmokakkskaq1sjg2t2y0nxx9'}
        Words are extracted by the 'text' field.
        The list of tweets comes in chronological order from newest to oldest. Hence the tweets are traversed
        in reverse order.

        :param words: The number of unique words to be parsed.
        :param topic: The topic of the tweets
        :type topic: str
        :param fmt: The format of the response. Accepted "csv" | "json"
        :type fmt: str
        :type words: int

        :raises: TweetyParserException if tweets are empty
        :returns: A dictionary containing the timestamp of the first and last tweet
        as well as a list of the words found in descending order. If the format specified is csv, then the words
        will be comma separated instead of list.
        If the number of words requested is too big then it will return the maximum unique words found in the tweets
        Example:
        {
            words: list | str
            topic: str
            first_tweet_timestamp: str
            last_tweet_timestamp: str
        }
        :rtype: dict
        """
        if not tweets:
            detail = "Insufficient number of tweets provided by the Twitter API. Please try again later."
            raise exceptions.TweetyParserException(detail=detail)

        word_set = set()
        first_tweet_timestamp = self._extract_first_timestamp(tweets)
        last_tweet_timestamp = ""

        for i in range(len(tweets) - 1, -1, -1):
            tweet = tweets[i]
            if text := tweet.get('text'):
                tokens = self._tokenize_tweet_text(text)
                tokens_size = len(tokens)
                if len(word_set) + tokens_size == words:
                    word_set.update(tokens)
                    last_tweet_timestamp = tweet['created_at']
                    break
                elif len(word_set) + tokens_size < words:
                    word_set.update(tokens)
                else:
                    # tokens + word_set > words so add abs(words - len(word_set)) to words_set
                    diff = abs(words - len(word_set))
                    word_set.update(list(tokens)[:diff])
                    last_tweet_timestamp = tweet['created_at']
                    break

        if len(word_set) < words:
            message = f"Number of words requested: {words} was bigger than that in the number" \
                      f" of tweets: {len(word_set)}.\nConsider increasing settings.MAX_TWEETS value."
            logger.warning(message)

        words = sorted(list(word_set))
        if fmt == 'csv':
            words = ", ".join(words)

        return {
            "words": words,
            "topic": topic,
            "first_tweet_timestamp": self._reformat_timezone_str(first_tweet_timestamp),
            "last_tweet_timestamp": self._reformat_timezone_str(last_tweet_timestamp)
        }


class TweetyCsvRenderer(CSVRenderer):
    header = ['words', 'topic', 'first_tweet_timestamp', "last_tweet_timestamp"]
