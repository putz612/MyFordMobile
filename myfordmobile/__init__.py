"""Mopar API."""

import os
import logging
# pylint: disable=wrong-import-position
import json
try:
    from json.decoder import JSONDecodeError
except ImportError:
    JSONDecodeError = ValueError
import pickle
import time
import requests
from requests.auth import AuthBase
from bs4 import BeautifulSoup


_LOGGER = logging.getLogger(__name__)
HTML_PARSER = 'html.parser'
SIGNIN_URL = 'https://www.mopar.com/sign-in'


def _login:
    """Login"""