import re
from flask import current_app
from celery.utils.log import get_task_logger

from fizzbuzz_core import celery
from fizzbuzz_core.data.models import Authentication
from fizzbuzz_core.utils import fizzbuzz
from fizzbuzz_core.utils.twitter import Twitter


logger = get_task_logger(__name__)


@celery.task(name="periodic_task")
def answer_mentions():
    logger.info("Hello! from periodic task")
    twitter_client = Twitter(
        current_app.config['TW_CONSUMER_KEY'], current_app.config['TW_CONSUMER_SECRET'])

    auth = Authentication.query.order_by(Authentication.id.desc()).first()
    twitter_client.set_access_token(auth.oauth_token, auth.oauth_token_secret)

    mentions = twitter_client.get_mentions()
    answers = []
    username = twitter_client.me.screen_name
    for mention in mentions:
        try:
            text = re.sub(r'@[A-z0-9]+', '', mention.text).strip()
            text = fizzbuzz(int(text))

            answers.append({
                'username': mention.user.screen_name,
                'text': text,
                'to': username,
            })

            twitter_client.tweet(
                '@' + mention.user.screen_name + ' ' + text, in_reply_to=mention.id)
        except ValueError:
            print('Invalid number')
    logger.info("Ended")
