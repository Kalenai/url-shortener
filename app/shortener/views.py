from . import shortener


@shortener.route('/')
def index():
    return "hello world!"
