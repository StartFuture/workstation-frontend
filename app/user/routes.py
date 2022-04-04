from flask import render_template, request, redirect, url_for, flash, jsonify

from user import bp

@bp.route('/')
def index():
    return redirect(url_for('main.index'))


@bp.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        return jsonify({'status': 'ok'})
    
    elif request.method == 'GET':
        return render_template('user/login.html')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    
    if request.method == 'POST':
        return jsonify({'status': 'ok'})
    
    elif request.method == 'GET':
        return render_template('user/register.html')
    
    
@bp.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    
    if request.method == 'POST':
        return jsonify({'status': 'ok'})
    
    elif request.method == 'GET':
        # return render_template('user/reset_password.html')
        return 'reset_password'
        
    
@bp.route('/valid_code', methods=['GET', 'POST'])
def valid_code():
    
    if request.method == 'POST':
        return jsonify({'status': 'ok'})
    
    elif request.method == 'GET':
        # return render_template('user/valid_code.html')
        return 'valid_code'
        



