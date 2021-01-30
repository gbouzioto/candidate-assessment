"""
General utility functions and classes
"""
import searchtweets
from django.conf import settings

from . import constants as c

search_args = searchtweets.load_credentials(settings.SEARCH_TWEETS_CREDENTIAL_FILE,
                                            yaml_key=c.SEARCH_TWEETS_KEY,
                                            env_overwrite=False)
