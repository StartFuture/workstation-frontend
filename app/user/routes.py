from flask import render_template, request, redirect, url_for, flash, jsonify
import logging
from user import bp

@bp.route('/')
def index():
    return redirect(url_for('main.index'))


@bp.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':

        infos = request.form.to_dict()

        dict_front_login = {
            "user_login": infos["login"],
            "password_user": infos["password"]
        }

        return dict_front_login

    elif request.method == 'GET':
        return render_template('user/login/login.html')

@bp.route('/code', methods=['GET', 'POST'])
def code():
    
    if request.method == 'POST':
        infos = request.form.to_dict()

        dict_front_code = {
            "code_user": infos['cod_user'],
            "email": infos['email']
        }
    
        return dict_front_code

    elif request.method == 'GET':

        return render_template('user/login/login_autenticacao.html')        

@bp.route('/register', methods=['GET', 'POST'])
def register():
    
    if request.method == 'POST':
        infos = request.form.to_dict()
        
        full_name = infos['username']
        full_name = full_name.split(' ')
        last_name = ''
        for pos, names in enumerate(full_name):
            if pos == 0:
                name = names
            else:
                last_name += ' ' + names
                last_name

        dict_front_register = {
        "nome": name,
        "sobrenome": last_name.lstrip(),
        "data_aniversario": infos["birthday"],
        "sexo": infos["sexo"],
        "telefone": infos["phone"],
        "email": infos["email"],
        "senha": infos["password"],
        "cpf_cnpj": infos["cpf_cnpj"]
        }

        return dict_front_register
    elif request.method == 'GET':
        return render_template('user/register/cadastro.html')
    
    
@bp.route('/reset/password', methods=['GET', 'POST'])
def reset_password():
    
    if request.method == 'POST':
        infos = request.form.to_dict()

        dict_reset_password = {
            "email": infos['email']
        }

        return dict_reset_password

    elif request.method == 'GET':
        return render_template('user/reset_password/trocar-senha.html')


@bp.route('/valid/code', methods=['GET', 'POST'])
def valid_code():
    
    if request.method == 'POST':
        infos = request.form.to_dict()

        dict_valid_code = {
            "cod_user": infos['cod_user']
        }

        return dict_valid_code
    
    elif request.method == 'GET':
        return render_template('user/reset_password/recuperacao-conta.html')


@bp.route('/change/password', methods=['GET', 'POST'])
def change_password():
    
    if request.method == 'POST':
        infos = request.form.to_dict()

        dict_change_password = {
            "new_password": infos['new_password']
        }

        return dict_change_password
    
    elif request.method == 'GET':
        return render_template('user/reset_password/redefinicao-senha.html')

@bp.route('/profile', methods=['GET', 'POST'])
def profile():
    
    if request.method == 'POST':
        infos = request.form.to_dict()

        logging.warning(infos)

        return render_template('user/profile.html')
    
    elif request.method == 'GET':
        return render_template('user/profile.html')



        



