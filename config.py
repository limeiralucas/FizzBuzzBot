import os


class BaseConfig(object):
    """ Base config class. """
    ORIGINS = ['*']
    SECRET_KEY = ''


class Development(BaseConfig):
    """ Development config """

    PORT = 5000
    DEBUG = True
    TESTING = True
    ENV = 'dev'
    APPNAME = 'FizzBuzzBot_Dev'

    DB_HOST = 'localhost'
    DB_USER = 'fizzbuzz'
    DB_PASSWORD = 'f1zz$buzz'
    DB_NAME = 'fizzbuzz_db'

    SQLALCHEMY_DATABASE_URI = 'mysql://{user}:{pwd}@{host}/{db}'.format(
        user=DB_USER,
        pwd=DB_PASSWORD,
        host=DB_HOST,
        db=DB_NAME,
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Production(BaseConfig):
    """ Production config """

    PORT = 4687
    DEBUG = False
    TESTING = False
    ENV = 'production'
    APPNAME = 'FizzBuzzBot'

    DB_HOST = os.getenv('DB_HOST')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_NAME = os.getenv('DB_NAME')

    SQLALCHEMY_DATABASE_URI = 'mysql://{user}:{pwd}@{host}/{db}'.format(
        user=DB_USER,
        pwd=DB_PASSWORD,
        host=DB_HOST,
        db=DB_NAME,
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
