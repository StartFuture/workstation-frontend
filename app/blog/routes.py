from flask import render_template, request, redirect, url_for, flash, jsonify

from blog import bp

import utils, parameters, functions, authorization

@bp.route('/')
@authorization.is_not_auth
def index_blog():
    return render_template('blog/blog.html')



