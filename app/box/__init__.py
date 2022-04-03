from flask import Blueprint

bp = Blueprint('box', __name__, url_prefix='/box')

from box import routes