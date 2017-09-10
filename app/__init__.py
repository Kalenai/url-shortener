from flask import Flask
from app.shortener import shortener


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    app.register_blueprint(shortener)

    return app
