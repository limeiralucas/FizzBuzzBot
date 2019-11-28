import re
from redis import Redis
from flask import current_app
from celery.utils.log import get_task_logger

from fizzbuzz_core import celery
from fizzbuzz_core.data.models import Interaction, db
from fizzbuzz_core.utils import fizzbuzz
from fizzbuzz_core.utils.twitter import Twitter


logger = get_task_logger(__name__)


@celery.task(name="periodic_task")
def answer_mentions():
    twitter_client = Twitter(
        current_app.config['TW_CONSUMER_KEY'], current_app.config['TW_CONSUMER_SECRET'])

    twitter_client.set_access_token(
        current_app.config['TW_OAUTH_TOKEN'], current_app.config['TW_OAUTH_TOKEN_SECRET'])

    redis_client = Redis(
        current_app.config['REDIS_HOST'], port=6379, db=current_app.config['REDIS_DB'])

    last_tweet_id = redis_client.get('last_tweet_id')

    mentions = twitter_client.get_mentions(since_id=last_tweet_id)
    if len(mentions) > 0:
        redis_client.set('last_tweet_id', mentions[0].id)
        for mention in mentions:
            text = re.sub(r'@[A-z0-9]+', '', mention.text).strip()
            try:
                text = fizzbuzz(int(text))

                tweet = '@' + mention.user.screen_name + ' ' + str(text)
                twitter_client.tweet(tweet, in_reply_to=mention.id)

                new_interaction = Interaction(
                    mention.user.screen_name, mention.text, tweet)
                db.session.add(new_interaction)
                db.session.commit()
            except Exception:
                twitter_client.tweet('Invalid number', in_reply_to=mention.id)
