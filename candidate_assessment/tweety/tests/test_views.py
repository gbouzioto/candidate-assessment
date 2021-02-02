""" Unittests for views file"""
from unittest import mock

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.renderers import JSONRenderer
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from . import mock_constants as mc
from .. import utils
from .. import exceptions


class AuthenticatedEndpointBaseTestCase(APITestCase):
    """ Base class with moc"""

    @classmethod
    def setUpClass(cls):
        super(AuthenticatedEndpointBaseTestCase, cls).setUpClass()
        cls.user = User.objects.create_user(username='foobarbuz',
                                            password='top_secret')
        cls.token = Token.objects.create(user=cls.user)
        cls.token.save()


class HelloAPIViewTestCase(AuthenticatedEndpointBaseTestCase):
    """ Class for testing HelloAPIView """

    @classmethod
    def setUpClass(cls):
        super(HelloAPIViewTestCase, cls).setUpClass()
        cls.url = reverse('tweety-api:home')

    def test_happy_path(self):
        """ HelloAPIView get request with authenticated user"""

        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)
        expected_data = {"message": "Hello my name is Tweety!"}

        self.assertDictEqual(response.data, expected_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unhappy_path_unauthorized(self):
        """ HelloAPIView get request with not an authenticated user"""

        response = self.client.get(self.url)
        expected_data = {"detail": "Authentication credentials were not provided."}

        self.assertDictEqual(response.data, expected_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class UserRegisterAPIViewTestCase(APITestCase):
    """ Class for testing UserRegisterAPIView """

    @classmethod
    def setUpClass(cls):
        super(UserRegisterAPIViewTestCase, cls).setUpClass()
        cls.url = reverse('tweety-api:register')
        cls.username = "foobarbuz"
        cls.password = "foobar123!"

    def test_happy_path(self):
        """ UserRegisterAPIView post request happy path"""

        data = {"username": self.username,
                "password": self.password}
        response = self.client.post(self.url, data=data)
        user = User.objects.get(username=self.username)
        expected_message = f"User: {self.username} registered successfully."
        expected_data = {
            'success': 'True',
            'status code': status.HTTP_200_OK,
            'message': expected_message,
        }

        self.assertIsNotNone(user)
        self.assertDictEqual(response.data, expected_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unhappy_path_bad_request(self):
        """ UserRegisterAPIView post request unhappy path"""

        missing_username = {"username": ["This field is required."]}
        missing_password = {"password": ["This field is required."]}
        missing_credentials = {**missing_password, **missing_username}

        data = {"username": self.username}
        response = self.client.post(self.url, data=data)

        self.assertDictEqual(response.data, missing_password)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        data = {"password": self.password}
        response = self.client.post(self.url, data=data)

        self.assertDictEqual(response.data, missing_username)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        data = {}
        response = self.client.post(self.url, data=data)

        self.assertDictEqual(response.data, missing_credentials)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TweetWordCloudAPIViewTestCase(AuthenticatedEndpointBaseTestCase):
    """ Class for testing TweetWordCloudAPIView """

    @classmethod
    def setUpClass(cls):
        super(TweetWordCloudAPIViewTestCase, cls).setUpClass()
        cls.url = reverse('tweety-api:tweet-word-cloud')
        cls.json_cloud = mc.JSON_100_WORD_CLOUD
        cls.csv_cloud = mc.CSV_100_WORD_CLOUD

    @mock.patch("tweety.views.collect_results", new=mock.Mock())
    @mock.patch("tweety.views.gen_request_parameters", new=mock.Mock())
    @mock.patch("tweety.utils.search_args", new=mock.Mock())
    def test_happy_path(self):
        """ Successful TweetWordCloudAPIView post request with authenticated user"""

        self.client.force_authenticate(user=self.user)
        data = {
            "words": 100,
            "response_format": 'json'
        }

        with mock.patch("tweety.utils.TweetTextParser.extract_word_cloud") as mock_cloud_func:
            mock_cloud_func.return_value = self.json_cloud
            response = self.client.post(self.url, data=data)

        self.assertIsInstance(response.accepted_renderer, JSONRenderer)
        self.assertEqual(response.data, self.json_cloud)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {
            "words": 100,
            "response_format": 'csv'
        }

        with mock.patch("tweety.utils.TweetTextParser.extract_word_cloud") as mock_cloud_func:
            mock_cloud_func.return_value = self.csv_cloud
            response = self.client.post(self.url, data=data)

        self.assertIsInstance(response.accepted_renderer, utils.TweetyCsvRenderer)
        self.assertEqual(response.data, self.csv_cloud)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unhappy_path_unauthorized(self):
        """ TweetWordCloudAPIView get request with not an authenticated user """

        response = self.client.post(self.url)
        expected_data = {"detail": "Authentication credentials were not provided."}

        self.assertDictEqual(response.data, expected_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unhappy_path_bad_request(self):
        """ TweetWordCloudAPIView post request unhappy path """

        self.client.force_authenticate(user=self.user)

        # Missing payload
        missing_response_format = {"response_format": ["This field is required."]}
        missing_words = {"words": ["This field is required."]}
        missing_payload = {**missing_response_format, **missing_words}

        # Invalid words format
        wrong_words_format_1 = {"words": "dsd100", "response_format": "json"}
        wrong_words_format_2 = {"words": -1, "response_format": "json"}
        wrong_words_format_3 = {"words": 0, "response_format": "json"}
        invalid_integer = {"words": ["A valid integer is required."]}
        integer_greater_than_one = {"words": ["Ensure this value is greater than or equal to 1."]}

        # Invalid words format
        wrong_response_format_format_1 = {"words": 1000, "response_format": "fooo"}
        wrong_response_format_format_2 = {"words": 1000, "response_format": "111"}
        invalid_choice = {"response_format": ["valid choices are 'json' or 'csv'"]}

        data = {"words": 100}
        response = self.client.post(self.url, data=data)

        self.assertDictEqual(response.data, missing_response_format)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        data = {"response_format": "json"}
        response = self.client.post(self.url, data=data)

        self.assertDictEqual(response.data, missing_words)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        data = {}
        response = self.client.post(self.url, data=data)

        self.assertDictEqual(response.data, missing_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        data = wrong_words_format_1
        response = self.client.post(self.url, data=data)

        self.assertDictEqual(response.data, invalid_integer)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        data = wrong_words_format_2
        response = self.client.post(self.url, data=data)

        self.assertDictEqual(response.data, integer_greater_than_one)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        data = wrong_words_format_3
        response = self.client.post(self.url, data=data)

        self.assertDictEqual(response.data, integer_greater_than_one)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        data = wrong_response_format_format_1
        response = self.client.post(self.url, data=data)

        self.assertDictEqual(response.data, invalid_choice)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        data = wrong_response_format_format_2
        response = self.client.post(self.url, data=data)

        self.assertDictEqual(response.data, invalid_choice)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @mock.patch("tweety.views.collect_results", new=mock.Mock())
    @mock.patch("tweety.views.gen_request_parameters", new=mock.Mock())
    @mock.patch("tweety.utils.search_args", new=mock.Mock())
    def test_unhappy_path_parser_exception(self):
        """ TweetWordCloudAPIView post request unhappy path parser exception"""
        self.client.force_authenticate(user=self.user)
        data = {
            "words": 100,
            "response_format": 'json'
        }
        err_msg = "Random error occured in parsing."
        expected_response = {"detail": err_msg}

        with mock.patch("tweety.utils.TweetTextParser.extract_word_cloud") as mock_cloud_func:
            mock_cloud_func.side_effect = exceptions.TweetyParserException(detail=err_msg)
            response = self.client.post(self.url, data=data)

        self.assertDictEqual(response.data, expected_response)
        self.assertEqual(response.status_code, status.HTTP_503_SERVICE_UNAVAILABLE)

    @mock.patch("tweety.views.collect_results", new=mock.Mock())
    def test_unhappy_path_generic_exception(self):
        """ TweetWordCloudAPIView post request unhappy path generic exception"""
        self.client.force_authenticate(user=self.user)
        data = {
            "words": 100,
            "response_format": 'json'
        }

        expected_response = {
            "detail": "Error creating daily word cloud. Contact support for more info."
        }

        with mock.patch("tweety.views.collect_results") as mock_collect_res_func:
            mock_collect_res_func.side_effect = Exception()
            response = self.client.post(self.url, data=data)

        self.assertDictEqual(response.data, expected_response)
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
