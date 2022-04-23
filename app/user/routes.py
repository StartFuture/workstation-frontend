from flask import render_template, request, redirect, url_for, flash, jsonify
import logging
from user import bp
import utils

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
    
    dict_user_example = {
            'id_user': 1,
            'username' : 'Lucas Nunes',
            'email' : 'lucas@gmail.com',
            'password' : '1234',
            'cpf_cnpj' : '000.000.000-00',
            'telefone' : '0000-0000',
            'credit_card' : '0000 0000 0000 0000',
        }
        
    list_reservations = [
        {
            'id' : '1',
            'box': 'Box Faria Lima',
            'details': '18 de março de 2022 (4 horas - 13:00 às 17:00)'
        },
        {
            'id' : '2',
            'box': 'Box Faria Lima 2',
            'details': '20 de março de 2022 (4 horas - 13:00 às 17:00)'
        },
    ]
    
    if request.method == 'POST':

        valid_inputs = ['username','email','password','cpf_cnpj','telefone','credit_card']
        
        infos = request.form.to_dict()
        
        logging.warning(infos)
        
        id_user = infos['id_user']
        
        key = list(infos.keys())[1]
        value = list(infos.values())[1]
        
        if key in valid_inputs:
            if key == 'username':
                utils.update_username(id_user, value)
            elif key == 'email':
                utils.update_email(id_user, value)
            elif key == 'password':
                utils.update_password(id_user, value)
            elif key == 'cpf_cnpj':
                utils.update_cpf_cnpj(id_user, value)
            elif key == 'telefone':
                utils.update_telefone(id_user, value)
            elif key == 'credit_card':
                utils.update_credit_card(id_user, value)

        return render_template('user/perfil.html', dict_user=dict_user_example, list_reservations=list_reservations)
    
    elif request.method == 'GET':
        
        return render_template('user/perfil.html', dict_user=dict_user_example, list_reservations=list_reservations)



        



