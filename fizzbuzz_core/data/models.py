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
