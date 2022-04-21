from flask import render_template, request, redirect, url_for, flash, jsonify

from main import bp

@bp.route('/')
def index():
    return render_template('main/index.html')


@bp.route('/about')
def about():
    return render_template('main/about.html')


