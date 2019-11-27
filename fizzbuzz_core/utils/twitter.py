from flask import current_app
import oauth2 as oauth
import urllib

request_token_url = 'https://api.twitter.com/oauth/request_token'
access_token_url = 'https://api.twitter.com/oauth/access_token'
authorize_url = 'https://api.twitter.com/oauth/authorize'


def get_request_token():
    CONSUMER_KEY = current_app.config['TW_CONSUMER_KEY']
    CONSUMER_SECRET = current_app.config['TW_CONSUMER_SECRET']

    consumer = oauth.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
    client = oauth.Client(consumer)
    resp, content = client.request(request_token_url, "GET")
    if resp['status'] != '200':
        raise Exception("Invalid response {}".format(resp['status']))

    return dict(urllib.parse.parse_qsl(content.decode("utf-8")))


def get_twitter_auth_url(request_token):
    return "{0}?oauth_token={1}".format(
        authorize_url, request_token['oauth_token'])


def get_oauth_token(request_token, oauth_verifier):
    token = oauth.Token(request_token['oauth_token'],
                        request_token['oauth_token_secret'])
    token.set_verifier(oauth_verifier)

    return token


def get_twitter_access_token(token):
    CONSUMER_KEY = current_app.config['TW_CONSUMER_KEY']
    CONSUMER_SECRET = current_app.config['TW_CONSUMER_SECRET']

    consumer = oauth.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
    client = oauth.Client(consumer, token)
    _, content = client.request(access_token_url, "POST")
    access_token = dict(urllib.parse.parse_qsl(content.decode("utf-8")))

    return access_token
