from random import choice
from flask import abort, jsonify, redirect, render_template, request
from sqlalchemy.orm import exc
from validators import url
from . import shortener
from .. import db, wordlist
from ..models import UrlLink


@app.before_first_request
def create_database():
     db.create_all()


@shortener.route('/')
def index():
    """
    Returns the site index.
    """
    return render_template('index.html')


@shortener.route('/new/<path:url_input>')
def get_shortened_url(url_input):
    """
    Returns a new URL link to redirect to the URL that was passed in.
    Returns error code 400 if the URL is not valid.
    """
    try:
        if not url(url_input):
            raise ValueError
        while True:
            url_key = choice(wordlist.first_list) + '-' + choice(wordlist.second_list)
            if not UrlLink.query.filter_by(url_key=url_key).first():
                new_url_link = UrlLink(url_key, url_input)
                db.session.add(new_url_link)
                db.session.commit()
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
        query = UrlLink.query.filter_by(url_key=url_key_input).first()
        if query:
            query.update_last_used()
            db.session.commit()
            return redirect(query.url)
        else:
            raise exc.NoResultFound
    except exc.NoResultFound:
        abort(404)
