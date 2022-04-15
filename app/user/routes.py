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
        return render_template('login_page/login.html')
        

@bp.route('/register', methods=['GET', 'POST'])
def register():
    
    if request.method == 'POST':
        return jsonify({'status': 'ok'})
    
    elif request.method == 'GET':
        return render_template('login_page/cadastro.html')
    
    
@bp.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    
    if request.method == 'POST':
        return jsonify({'status': 'ok'})
    
    elif request.method == 'GET':
        return render_template('login_page/trocar-senha.html')
        
        
@bp.route('/change_password', methods=['GET', 'POST'])
def change_password():
    
    if request.method == 'POST':
        return jsonify({'status': 'ok'})
    
    elif request.method == 'GET':
        return render_template('login_page/redefinicao-senha.html')
        
    

@bp.route('/valid_code', methods=['GET', 'POST'])
def valid_code():
    
    if request.method == 'POST':
        return jsonify({'status': 'ok'})
    
    elif request.method == 'GET':
        return render_template('login_page/recuperacao-conta.html')
        
        



