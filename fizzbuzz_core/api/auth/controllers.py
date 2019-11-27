from flask import Blueprint, jsonify, request, current_app, redirect

from fizzbuzz_core.utils.twitter import get_request_token, get_twitter_auth_url

auth = Blueprint('user', __name__)


@auth.route('/login', methods=['GET'])
def login():
    request_token = get_request_token()
    url = get_twitter_auth_url(request_token)

    redirect(url)


@auth.route('/twhook', methods=['GET'])
def twitter_login_webhook():
    print(request.args)

    return jsonify({'status': 'ok'})
