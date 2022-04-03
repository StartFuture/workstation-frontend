from flask import render_template, request, redirect, url_for, flash, jsonify

from billing import bp

@bp.route('/')
def index_billing():
    return 'teste route billing'



