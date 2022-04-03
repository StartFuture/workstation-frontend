from flask import render_template, request, redirect, url_for, flash, jsonify

from box import bp

@bp.route('/')
def index_box():
    return 'teste route box'



