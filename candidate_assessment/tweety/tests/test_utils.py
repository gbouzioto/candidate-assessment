from unittest import mock
from copy import deepcopy
from rest_framework.test import APITestCase

from . import mock_constants as mc
from .. import utils
from .. import exceptions


class TestTweetTextParserTestCase(APITestCase):
    """Class for testing the utils file"""

    @classmethod
    def setUpClass(cls):
        """Setup class"""
        super(TestTweetTextParserTestCase, cls).setUpClass()
        cls.parser = utils.TweetTextParser()
        # mock tweets from Twitter API
        cls.tweets = mc.MOCK_TWEETS
        # a tweet from the above tweets
        cls.tweet = mc.MOCK_TWEET
        cls.topic = "covid"

    def test_tokenize_text_tweet(self):
        """ Tests TestTweetTextParser._tokenize_tweet_text method """

        expected_result = {'tune', 'into', 'the', 'health', 'and', 'humor', 'show', 'with', 'on', 'healthnews',
                           'including', 'how', 'to', 'beat', 'covid', 'this', 'year', 'your', 'wellnessiq', 'and',
                           'heartattacks', 'could', 'be', 'predicted', 'in', 'advance', 'with', 'simple', 'xray'}
        self.assertSetEqual(self.parser._tokenize_tweet_text(self.tweet["text"]),
                            expected_result)

    def test_reformat_timezone_str(self):
        """ Tests TestTweetTextParser._reformat_timezone_str method """

        expected_result_1 = '01-02-2021 09:00:00 UTC'
        self.assertEqual(self.parser._reformat_timezone_str(self.tweet["created_at"]), expected_result_1)

        # empty string case
        expected_result_2 = ""
        self.assertEqual(self.parser._reformat_timezone_str(""), expected_result_2)

    def test_extract_first_timestamp_happy_path(self):
        """ Tests TestTweetTextParser._extract_first_timestamp method success scenario """

        expected_result = '2021-02-01T09:00:00.000Z'
        self.assertEqual(self.parser._extract_first_timestamp(self.tweets), expected_result)

    @mock.patch("tweety.utils.logger")
    def test_extract_first_timestamp_unhappy_path(self, mock_logger):
        """ Tests TestTweetTextParser._extract_first_timestamp method failure scenario """

        err_msg = "Could not retrieve timestamp value from tweets provided by the Twitter API. Please try again later."

        # remove the "created_at" key from a few tweets
        tweets = self.tweets[:4]
        tweets = deepcopy(tweets)
        for tweet in tweets:
            del tweet["created_at"]

        with self.assertRaises(exceptions.TweetyParserException) as cm:
            self.parser._extract_first_timestamp(tweets)

        err = cm.exception
        mock_logger.error.assert_called_once()
        self.assertEqual(err.detail, err_msg)

    def test_extract_word_cloud_happy_path_json(self):
        """ Tests TestTweetTextParser._extract_first_timestamp method success json scenario """
        expected_cloud = mc.MOCK_CLOUD_SUCCESS
        words = 100
        fmt = "json"

        res_1 = self.parser.extract_word_cloud(deepcopy(self.tweets), words, self.topic)

        self.assertEqual(expected_cloud["topic"], res_1["topic"])
        self.assertEqual(expected_cloud["first_tweet_timestamp"], res_1["first_tweet_timestamp"])
        self.assertEqual(expected_cloud["last_tweet_timestamp"], res_1["last_tweet_timestamp"])
        self.assertIsInstance(res_1["words"], list)
        self.assertEqual(len(res_1["words"]), expected_cloud["words"])

        res_2 = self.parser.extract_word_cloud(deepcopy(self.tweets), words, self.topic, fmt)

        self.assertEqual(expected_cloud["topic"], res_2["topic"])
        self.assertEqual(expected_cloud["first_tweet_timestamp"], res_2["first_tweet_timestamp"])
        self.assertEqual(expected_cloud["last_tweet_timestamp"], res_2["last_tweet_timestamp"])
        self.assertIsInstance(res_2["words"], list)
        self.assertEqual(len(res_2["words"]), expected_cloud["words"])

    def test_extract_word_cloud_happy_path_csv(self):
        """ Tests TestTweetTextParser._extract_first_timestamp method success csv scenario """
        expected_cloud = mc.MOCK_CLOUD_SUCCESS
        words = 100
        fmt = "csv"

        res = self.parser.extract_word_cloud(deepcopy(self.tweets), words, self.topic, fmt)

        self.assertEqual(expected_cloud["topic"], res["topic"])
        self.assertEqual(expected_cloud["first_tweet_timestamp"], res["first_tweet_timestamp"])
        self.assertEqual(expected_cloud["last_tweet_timestamp"], res["last_tweet_timestamp"])
        self.assertIsInstance(res["words"], str)
        self.assertEqual(len(res["words"].split(", ")), expected_cloud["words"])

    @mock.patch("tweety.utils.logger")
    def test_extract_word_cloud_happy_path_maximum_words_reached_json(self, mock_logger):
        """ Tests TestTweetTextParser._extract_first_timestamp method success json scenario
        where the the number of words requested was bigger than the one in the tweets"""
        expected_cloud = mc.MOCK_MAX_CLOUD
        words = 1000
        fmt = 'json'

        res = self.parser.extract_word_cloud(deepcopy(self.tweets), words, self.topic, fmt)

        self.assertEqual(expected_cloud["topic"], res["topic"])
        self.assertEqual(expected_cloud["first_tweet_timestamp"], res["first_tweet_timestamp"])
        self.assertEqual(expected_cloud["last_tweet_timestamp"], res["last_tweet_timestamp"])
        self.assertIsInstance(res["words"], list)
        self.assertEqual(len(res["words"]), expected_cloud["words"])
        mock_logger.warning.assert_called_once()

    @mock.patch("tweety.utils.logger")
    def test_extract_word_cloud_happy_path_maximum_words_reached_csv(self, mock_logger):
        """ Tests TestTweetTextParser._extract_first_timestamp method success csv scenario
        where the the number of words requested was bigger than the one in the tweets"""
        expected_cloud = mc.MOCK_MAX_CLOUD
        words = 1000
        fmt = 'csv'

        res = self.parser.extract_word_cloud(deepcopy(self.tweets), words, self.topic, fmt)

        self.assertEqual(expected_cloud["topic"], res["topic"])
        self.assertEqual(expected_cloud["first_tweet_timestamp"], res["first_tweet_timestamp"])
        self.assertEqual(expected_cloud["last_tweet_timestamp"], res["last_tweet_timestamp"])
        self.assertIsInstance(res["words"], str)
        self.assertEqual(len(res["words"].split(", ")), expected_cloud["words"])
        mock_logger.warning.assert_called_once()

    def test_extract_word_cloud_un_happy_path(self):
        """ Tests TestTweetTextParser._extract_first_timestamp method unhappy path"""

        err_msg = "Insufficient number of tweets provided by the Twitter API. Please try again later."
        tweets = []
        words = 10

        with self.assertRaises(exceptions.TweetyParserException) as cm:
            self.parser.extract_word_cloud(tweets, words, self.topic)

        err = cm.exception
        self.assertEqual(err.detail, err_msg)
