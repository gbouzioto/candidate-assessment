from rest_framework import status
from rest_framework.exceptions import APIException


class TweetyGeneralException(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = 'Internal server error, please try again later.'
    default_code = 'internal_server_error'