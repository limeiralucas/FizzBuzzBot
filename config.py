import os


class BaseConfig(object):
    """ Base config class. """
    ORIGINS = ['*']
    SECRET_KEY = ''

    DEBUG = False
    TESTING = False
    ENV = ''
    APPNAME = ''

    TW_CONSUMER_KEY = os.getenv('TW_CONSUMER_KEY')
    TW_CONSUMER_SECRET = os.getenv('TW_CONSUMER_SECRET')
    TW_APP_BEARER = os.getenv('TW_APP_BEARER')

    TW_OAUTH_TOKEN = os.getenv('TW_OAUTH_TOKEN')
    TW_OAUTH_TOKEN_SECRET = os.getenv('TW_OAUTH_TOKEN_SECRET')

    REDIS_HOST = os.getenv('REDIS_HOST')
    REDIS_DB = os.getenv('REDIS_DB')

    DB_HOST = os.getenv('FZ_DB_HOST', 'localhost')
    DB_USER = os.getenv('FZ_DB_USER', 'fizzbuzz')
    DB_PASSWORD = os.getenv('FZ_DB_PWD', 'f1zzbuzz')
    DB_NAME = os.getenv('FZ_DB_NAME', 'fizzbuzz_db')

    SQLALCHEMY_DATABASE_URI = 'mysql://{user}:{pwd}@{host}/{db}'.format(
        user=DB_USER,
        pwd=DB_PASSWORD,
        host=DB_HOST,
        db=DB_NAME,
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CELERY_RESULT_BACKEND_HOST = os.getenv(
        'CELERY_RESULT_BACKEND_HOST', 'localhost')
    CELERY_RESULT_BACKEND_DB = os.getenv('CELERY_RESULT_BACKEND_DB', '0')
    CELERY_RESULT_BACKEND = 'redis://{host}:6379/{db}'.format(
        host=CELERY_RESULT_BACKEND_HOST, db=CELERY_RESULT_BACKEND_DB)

    BROKER_HOST = os.getenv('BROKER_HOST', 'localhost')
    BROKER_DB = os.getenv('BROKER_DB', '0')
    BROKER_URL = 'redis://{host}:6379/{db}'.format(
        host=BROKER_HOST, db=BROKER_DB)

    CELERY_SEND_TASK_SENT_EVENT = True


class DevelopmentConfig(BaseConfig):
    """ Development config """

    DEBUG = True
    TESTING = True
    ENV = 'dev'
    APPNAME = 'FizzBuzzBot_Dev'


class TestConfig(BaseConfig):
    """ Test config """

    DEBUG = True
    TESTING = True
    ENV = 'test'
    APPNAME = 'FizzBuzzBot_Test'


class ProductionConfig(BaseConfig):
    """ Production config """

    DEBUG = False
    TESTING = False
    ENV = 'production'
    APPNAME = 'FizzBuzzBot'
