from random import randrange
from flask import jsonify, request
from . import shortener
from .. import db
from ..models import UrlLink
from app.utils import generate_url_link_phrase


def create_new_url_link(url):
    # TODO Add URL validation
    while True:
        url_key = str(randrange(0, 9999)) + '-' + str(randrange(0, 9999))
        if not UrlLink.query.filter_by(url_key=url_key).first():
            new_url_link = UrlLink(url_key, url)
            db.session.add(new_url_link)
            return url_key


@shortener.route('/')
def index():
    return "hello world!"


@shortener.route('/new/<path:url>')
def get_shortened_url(url):
    """
    Returns a new URL link to redirect to the URL that was passed in.
    """
    url_key = create_new_url_link(url)
    return jsonify(original_url=url,
                   short_url=request.url_root + url_key)
