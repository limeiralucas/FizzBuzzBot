import requests
import urllib
import hmac
import base64
from flask import Blueprint, jsonify, request, current_app, redirect

from fizzbuzz_core.data.models import db, Authentication
from fizzbuzz_core.utils.twitter import Twitter

auth = Blueprint('auth', __name__)


@auth.route('/post', methods=['GET'])
def post():
    text = request.args.get('text')
    url = 'https://api.twitter.com/1.1/statuses/update.json'

    return {'status': 'ok'}


@auth.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    result = Twitter.search(query)

    return jsonify(result)


@auth.route('/login', methods=['GET'])
def login():
    twitter_client = Twitter(
        current_app.config['TW_CONSUMER_KEY'], current_app.config['TW_CONSUMER_SECRET'])

    url = twitter_client.get_authorization_url()
    request_token = twitter_client.get_request_token()

    new_auth = Authentication(request_token)
    db.session.add(new_auth)
    db.session.commit()

    return redirect(url)


@auth.route('/twhook', methods=['GET'])
def twitter_login_webhook():
    request_token = request.args.get('oauth_token')
    verifier = request.args.get('oauth_verifier')

    auth = Authentication.query.filter_by(
        request_token=request_token).first()

    if auth:
        twitter_client = Twitter(
            current_app.config['TW_CONSUMER_KEY'], current_app.config['TW_CONSUMER_SECRET'])

        oauth_token, oauth_token_secret = twitter_client.get_access_token(
            request_token, verifier)

        auth.oauth_token = oauth_token
        auth.oauth_token_secret = oauth_token_secret

        db.session.commit()

        return jsonify({'status': 'ok'})

    return jsonify({'status': 'error'})


@auth.route('/post', methods=['GET'])
def post_tweet():
    text = request.args.get('text')

    twitter_client = Twitter(
        current_app.config['TW_CONSUMER_KEY'], current_app.config['TW_CONSUMER_SECRET'])

    auth = Authentication.query.order_by(Authentication.id.desc()).first()
    twitter_client.set_access_token(auth.oauth_token, auth.oauth_token_secret)

    twitter_client.tweet(text)

    return {'status': 'ok'}
