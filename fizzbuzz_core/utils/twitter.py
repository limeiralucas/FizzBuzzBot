from flask import current_app
from base64 import b64encode
from datetime import datetime
import oauth2 as oauth
import urllib
import requests
import tweepy


class Twitter(object):
    auth = None

    def __init__(self, consumer_key, consumer_secret):
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    def get_authorization_url(self):
        try:
            return self.auth.get_authorization_url()
        except tweepy.TweepError:
            print('Error! Failed to get auth url')

    def get_request_token(self):
        return self.auth.request_token['oauth_token']

    def get_access_token(self, request_token, verifier):
        self.auth.request_token = {
            'oauth_token': request_token,
            'oauth_token_secret': verifier
        }

        try:
            self.auth.get_access_token(verifier)

            return self.auth.access_token, self.auth.access_token_secret
        except tweepy.TweepError:
            print('Error! Failed to get access token')

    def set_access_token(self, key, secret):
        self.auth.set_access_token(key, secret)

    def tweet(self, text=''):
        api = tweepy.API(self.auth)
        api.update_status('Please work!')

    @staticmethod
    def search(query=''):
        headers = {
            'Authorization': 'Bearer {}'.format(current_app.config['TW_APP_BEARER'])
        }
        print(headers)
        response = requests.get(
            'https://api.twitter.com/1.1/search/tweets.json?q={}'.format(query), headers=headers)

        return response.json()
