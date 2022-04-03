from flask import Blueprint

bp = Blueprint('user', __name__, url_prefix='/user')

from user import routes