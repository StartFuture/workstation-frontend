from flask import render_template, request, redirect, url_for, flash, jsonify
import logging
from user import bp

@bp.route('/')
def index():
    return redirect(url_for('main.index'))


@bp.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']

        dict_values_login = {
            "user_login": login,
            "password_user": password
        }
        pass
    elif request.method == 'GET':
        return render_template('user/login/login.html')

@bp.route('/code', methods=['GET', 'POST'])
def code():
    
    if request.method == 'POST':
        return jsonify({'status': 'ok'})
    
    elif request.method == 'GET':
        return render_template('user/login/login_autenticacao.html')        

@bp.route('/register', methods=['GET', 'POST'])
def register():
    
    if request.method == 'POST':
        infos = request.form.to_dict()
        pass
        
        
    
    elif request.method == 'GET':
        return render_template('user/register/cadastro.html')
    
    
@bp.route('/reset/password', methods=['GET', 'POST'])
def reset_password():
    
    if request.method == 'POST':
        return jsonify({'status': 'ok'})
    
    elif request.method == 'GET':
        return render_template('user/reset_password/trocar-senha.html')


@bp.route('/valid/code', methods=['GET', 'POST'])
def valid_code():
    
    if request.method == 'POST':
        return jsonify({'status': 'ok'})
    
    elif request.method == 'GET':
        return render_template('user/reset_password/recuperacao-conta.html')


@bp.route('/change/password', methods=['GET', 'POST'])
def change_password():
    
    if request.method == 'POST':
        return jsonify({'status': 'ok'})
    
    elif request.method == 'GET':
        return render_template('user/reset_password/redefinicao-senha.html')
        



