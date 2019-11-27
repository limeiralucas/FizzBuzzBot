from flask import Blueprint, jsonify, request, current_app, redirect

from fizzbuzz_core.data.models import db, Authentication
from fizzbuzz_core.utils.twitter import get_request_token, get_twitter_auth_url, get_oauth_token, get_twitter_access_token

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET'])
def login():
    request_token = get_request_token()
    url = get_twitter_auth_url(request_token)

    new_auth = Authentication(
        request_token['oauth_token'], request_token['oauth_token_secret'])
    db.session.add(new_auth)
    db.session.commit()

    return redirect(url)


@auth.route('/twhook', methods=['GET'])
def twitter_login_webhook():
    oauth_request_token = request.args.get('oauth_token')
    oauth_verifier = request.args.get('oauth_verifier')

    auth = Authentication.query.filter_by(
        oauth_request_token=oauth_request_token).first()

    if auth:
        request_token = {
            'oauth_token': oauth_request_token,
            'oauth_token_secret': auth.oauth_request_token_secret,
        }

        token = get_oauth_token(request_token, oauth_verifier)

        try:
            access_token = get_twitter_access_token(token)
            auth.oauth_token = access_token['oauth_token']
            auth.oauth_token_secret = access_token['oauth_token_secret']
            db.session.commit()

            print(access_token)

            return jsonify({'status': 'ok'})
        except:
            return jsonify({'status': 'error retrieving access_token'})

    return jsonify({'status': 'error'})


@auth.route('/webhook/twitter', methods=['GET'])
def twitter_webhook():
    # creates HMAC SHA-256 hash from incomming token and your consumer secret
    sha256_hash_digest = hmac.new(TWITTER_CONSUMER_SECRET, msg=request.args.get(
        'crc_token'), digestmod=hashlib.sha256).digest()

    # construct response data with base64 encoded hash
    response = {
        'response_token': 'sha256=' + base64.b64encode(sha256_hash_digest)
    }

    # returns properly formatted json response
    return json.dumps(response)
