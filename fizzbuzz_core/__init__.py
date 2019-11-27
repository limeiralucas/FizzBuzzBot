import os

from flask import Flask
from flask_cors import CORS

from fizzbuzz_core.data.models import db
from fizzbuzz_core.api.auth.controllers import auth
from config import BaseConfig


def create_app(environment):
    app = Flask(__name__)
    env = os.getenv('ENV', 'development')

    app.config.from_object(environment.get(env))

    cors = CORS(app, resources={
        r'/api/*': {
                'origins': BaseConfig.ORIGINS,
                }
    })

    app.url_map.strict_slashes = False

    db.init_app(app)

    app.register_blueprint(auth, url_prefix='/')

    return app
