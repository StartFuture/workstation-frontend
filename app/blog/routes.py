from flask import render_template, request, redirect, url_for, flash, jsonify

from blog import bp

@bp.route('/')
def index_blog():
    return render_template('blog/blog.html')



