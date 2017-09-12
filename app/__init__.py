from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.shortener import shortener


db = SQLAlchemy()


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    print(db)

    app.register_blueprint(shortener)

    return app
