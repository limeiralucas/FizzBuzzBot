import oauth2 as oauth
import urllib

CONSUMER_KEY = 'V3l01bqEYX7z2nvZu4zAryQ6V'
CONSUMER_SECRET = 'TU5BPg5nh5POuWydN12TiwQC2JmD7U5KEqOaIHMURE5eTWRHue'

request_token_url = 'https://api.twitter.com/oauth/request_token'
access_token_url = 'https://api.twitter.com/oauth/access_token'
authorize_url = 'https://api.twitter.com/oauth/authorize'


def get_request_token():
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
    consumer = oauth.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
    client = oauth.Client(consumer, token)
    resp, content = client.request(access_token_url, "POST")
    access_token = dict(urllib.parse.parse_qsl(content.decode("utf-8")))

    return access_token
