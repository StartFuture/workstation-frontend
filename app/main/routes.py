import requests

from flask import render_template, redirect, url_for, flash, jsonify, session

import authorization

from main import bp


@bp.route('/')
@authorization.is_not_auth
def index():
    profile = dict(session).get('profile', [])
    return render_template('main/index.html', profile=profile)

@bp.route('/about')
@authorization.is_not_auth
def about():
    profile = dict(session).get('profile', [])
    return render_template('main/about.html', profile=profile)

@bp.route('/health')
@authorization.is_auth
def health():
    return jsonify({"status": "UP"}, 200)