# from mock import Mock
import tweepy
import unittest
from tweet import main


class OAuthHandler(object):

    def __init__(self, consumer_key, consumer_secret):
        pass

    def set_access_token(self, access_key, access_secret):
        pass


class API(object):

    def __init__(self, auth_handler=None):
        pass

    def update_status(self, status=None):
        pass


tweepy.OAuthHandler = OAuthHandler
tweepy.API = API


class MainTest(unittest.TestCase):

    def test_main(self):
        main()


if __name__ == "__main__":
    unittest.main()
