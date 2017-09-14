from . import shortener
from app.utils import generate_url_link_phrase


@shortener.route('/')
def index():
    return "hello world!"


@shortener.route('/new/<url>')
def get_shortened_url(url):
    """
    Returns a new URL link to redirect to the URL that was passed in.
    """
    # TODO - check if url link already exists and create the link in the database
    return generate_url_link_phrase()
