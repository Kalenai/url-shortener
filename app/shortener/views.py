from random import choice
from flask import abort, jsonify, redirect, request
from sqlalchemy.orm import exc
from validators import url
from . import shortener
from .. import db, wordlist
from ..models import UrlLink


def create_new_url_link(url_input):
    """
    Checks that the URL input is valid, creates a new URL link, storing the pair in the database and returning it.
    Raises ValueError if the URL is invalid.
    """
    if not url(url_input):
        raise ValueError
    while True:
        url_key = choice(wordlist.first_list) + '-' + choice(wordlist.second_list)
        if not UrlLink.query.filter_by(url_key=url_key).first():
            new_url_link = UrlLink(url_key, url_input)
            db.session.add(new_url_link)
            db.session.commit()
            return url_key


def get_url_from_url_key(url_key_input):
    """
    Looks up the URL key passed in and returns the corresponding URL.
    Raises NoResultFound if it finds no URL link.
    """
    url_link = UrlLink.query.filter_by(url_key=url_key_input).first()
    if url_link:
        return url_link.url
    else:
        raise exc.NoResultFound


@shortener.route('/')
def index():
    """
    Returns the site index.
    """
    return str(wordlist.second_list)


@shortener.route('/new/<path:url_input>')
def get_shortened_url(url_input):
    """
    Returns a new URL link to redirect to the URL that was passed in.
    Returns error code 400 if the URL is not valid.
    """
    try:
        url_key = create_new_url_link(url_input)
        return jsonify(original_url=url_input,
                       short_url=request.url_root + url_key)
    except ValueError:
        abort(400)


@shortener.route('/<url_key_input>')
def redirect_to_url(url_key_input):
    """
    Looks up the URL key passed in and redirects to the original URL.
    Returns error code 400 if the URL key is not found in the database.
    """
    try:
        return redirect(get_url_from_url_key(url_key_input))
    except exc.NoResultFound:
        abort(404)
