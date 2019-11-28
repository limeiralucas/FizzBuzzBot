import os

from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

from fizzbuzz_core.data.models import db
from fizzbuzz_core.api.auth.controllers import auth
from config import BaseConfig


def create_app():
    app = Flask(__name__)
    env = os.getenv('ENV', 'development')
    cwd = os.getcwd()
    dotenv_path = os.path.join(cwd, '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path=dotenv_path)

    app.config.from_object('config.{}Config'.format(env.capitalize()))

    CORS(app, resources={
        r'/api/*': {
            'origins': BaseConfig.ORIGINS,
        }
    })

    app.url_map.strict_slashes = False

    db.init_app(app)

    app.register_blueprint(auth, url_prefix='/')

    return app
