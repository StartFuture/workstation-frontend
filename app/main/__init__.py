from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')

from main import routes