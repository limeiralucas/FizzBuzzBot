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

    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
    BROKER_URL = 'redis://localhost:6379/0'
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
