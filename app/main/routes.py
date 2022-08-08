from flask import render_template, redirect, url_for, flash, jsonify
import requests

from main import bp

@bp.route('/')
def index():
    return render_template('main/index.html')


@bp.route('/about')
def about():
    return render_template('main/about.html')

@bp.route('/health')
def health():
    return jsonify({"status": "UP"}, 200)

@bp.route('/test')
def test():
    user_email = 'lucas@gmail.com'
    password = '123456'
    
    value = requests.get('http://localhost:5000/login', json={'user_login': user_email, 'password_user': password})
    
    return jsonify({"status": "UP"}, 200)