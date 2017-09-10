from flask import Blueprint

shortener = Blueprint('shortener', __name__)

from . import views