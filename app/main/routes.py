import requests

from flask import render_template, redirect, url_for, flash, jsonify

import authorization

from main import bp


@bp.route('/')
@authorization.is_not_auth
def index():
    return render_template('main/index.html')

@bp.route('/about')
@authorization.is_not_auth
def about():
    return render_template('main/about.html')

@bp.route('/health')
@authorization.is_auth
def health():
    return jsonify({"status": "UP"}, 200)