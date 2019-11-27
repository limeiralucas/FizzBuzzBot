from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Interaction(db.Model):
    """ Model representing interactions with the bot """
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(100))
    message = db.Column(db.String(280))
    response = db.Column(db.String(280))
    date = db.Column(db.DateTime, default=db.func.now())

    def __init__(self, sender, message, response):
        self.sender = sender
        self.message = message
        self.response = response


class Authentication(db.Model):
    """ Model representing authentication proccess """
    id = db.Column(db.Integer, primary_key=True)
    oauth_request_token = db.Column(db.String(64))
    oauth_request_token_secret = db.Column(db.String(64))
    oauth_token = db.Column(db.String(64))
    oauth_token_secret = db.Column(db.String(64))

    def __init__(self, oauth_request_token, oauth_request_token_secret, oauth_token='', oauth_token_secret=''):
        self.oauth_request_token = oauth_request_token
        self.oauth_request_token_secret = oauth_request_token_secret
        self.oauth_token = oauth_token
        self.oauth_token_secret = oauth_token_secret
