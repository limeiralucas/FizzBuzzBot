import os

from flask import Flask, current_app
from flask_cors import CORS
from dotenv import load_dotenv
from celery import Celery

from flask import current_app
from fizzbuzz_core.data.models import db
from config import BaseConfig


celery = Celery()


def create_app(**kwargs):
    app = Flask(__name__)
    env = os.getenv('ENV', 'development')
    cwd = os.getcwd()
    dotenv_path = os.path.join(cwd, '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path=dotenv_path)

    app.config.from_object('config.{}Config'.format(env.capitalize()))
    celery.config_from_object(app.config)

    CORS(app, resources={
        r'/api/*': {
            'origins': BaseConfig.ORIGINS,
        }
    })

    app.url_map.strict_slashes = False

    db.init_app(app)

    return app
