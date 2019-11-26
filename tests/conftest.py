import pytest

from fizzbuzz_core import create_app
from fizzbuzz_core.data.models import db
from app import config


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app(config)

    testing_client = flask_app.test_client()
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()


@pytest.fixture(scope='module')
def init_database():
    db.create_all()
    db.session.commit()

    yield db

    db.drop_all()
