import datetime
from . import db


class UrlLink(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url_key = db.Column(db.String(128), unique=True, index=True, nullable=False)
    url = db.Column(db.String(2000), nullable=False)
    created = db.Column(db.DateTime, nullable=False)
    last_used = db.Column(db.DateTime)

    def __init__(self, url_key, url):
        self.url_key = url_key
        self.url = url
        self.created = datetime.datetime.utcnow()
        self.last_used = None

    def __repr__(self):
        return '<{url_key}: {url}>'.format(url_key=self.url_key, url=self.url)
