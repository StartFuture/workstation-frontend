from flask import render_template, request, redirect, url_for, flash, jsonify

from user import bp

@bp.route('/')
def index():
    return 'teste route user'



