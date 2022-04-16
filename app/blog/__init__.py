from flask import Blueprint

bp = Blueprint('blog', __name__, url_prefix='/blog')

from blog import routes