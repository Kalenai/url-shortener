from . import db


class UrlLink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url_key = db.Column(db.Text, unique=True)
    url = db.Column(db.Text)
