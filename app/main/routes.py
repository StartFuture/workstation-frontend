from flask import render_template, request, redirect, url_for, flash, jsonify

from main import bp

@bp.route('/')
def index():
    return 'index'


@bp.route('/about')
def about():
    return 'about'


@bp.route('/pricing')
def pricing():
    return 'pricing'


