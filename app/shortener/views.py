from random import choice
from flask import abort, jsonify, request
from validators import url
from . import shortener
from .. import db, wordlist
from ..models import UrlLink


def create_new_url_link(url_input):
    if not url(url_input):
        raise ValueError
    while True:
        # url_key = str(randrange(0, 9999)) + '-' + str(randrange(0, 9999))
        url_key = choice(wordlist.first_list) + '-' + choice(wordlist.second_list)
        if not UrlLink.query.filter_by(url_key=url_key).first():
            new_url_link = UrlLink(url_key, url_input)
            db.session.add(new_url_link)
            db.session.commit()
            return url_key


@shortener.route('/')
def index():
    return str(wordlist.second_list)


@shortener.route('/new/<path:url_input>')
def get_shortened_url(url_input):
    """
    Returns a new URL link to redirect to the URL that was passed in.
    """
    try:
        url_key = create_new_url_link(url_input)
        return jsonify(original_url=url_input,
                       short_url=request.url_root + url_key)
    except ValueError:
        abort(400)
