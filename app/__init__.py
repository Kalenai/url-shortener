from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.wordlistclass import wordlist


db = SQLAlchemy()


def create_app(config):
    """
    Flask application factory to create the app object.
    """
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)

    from app.shortener import shortener
    app.register_blueprint(shortener)

    return app
