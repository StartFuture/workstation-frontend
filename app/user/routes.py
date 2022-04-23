from flask import render_template, request, redirect, url_for, flash, jsonify, session
import logging
from user import bp
import utils
import parameters
import functions

dict_login = {
            "email": "mateustoni04@gmail.com",
            "senha": 12345
        }

@bp.route('/')
def index():
    return redirect(url_for('main.index'))


@bp.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':

        if request.form['login'] == dict_login['email']:
            if str(request.form['password']) == str(dict_login['senha']):
                return redirect(url_for('user.code'))
            else:
                return redirect(url_for('user.login'))
        else:
            return redirect(url_for('user.login'))

    elif request.method == 'GET':
        
        return render_template('user/login/login.html')

@bp.route('/code', methods=['GET', 'POST'])
def code():
    
    dict_code = {
        'code': 588634,
        'email': 'mateustoni04@gmail.com'
    }
    
    if request.method == 'POST':
        
        if str(request.form['cod_user']) == str(dict_code['code']):
            return redirect(url_for('box.confirm_box'))

    elif request.method == 'GET':
        
        functions.send_email(cod=dict_code['code'], client_email=dict_code['email'])

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
    
    email = 'mateustoni04@gmail.com'
    
    if request.method == 'POST':
        if request.form['email_recover'] == email:
            functions.send_email_password(cod='145544', client_email='mateustoni04@gmail.com')
            return redirect(url_for('user.valid_code'))

    elif request.method == 'GET':
        return render_template('user/reset_password/trocar-senha.html')


@bp.route('/valid/code', methods=['GET', 'POST'])
def valid_code():
    
    if request.method == 'POST':
        if str(request.form['code_user']) == str('145544'):
            return redirect(url_for('user.change_password'))
    
    elif request.method == 'GET':
        return render_template('user/reset_password/recuperacao-conta.html')


@bp.route('/change/password', methods=['GET', 'POST'])
def change_password():
    
    if request.method == 'POST':
        dict_login['senha'] = request.form['senha_recover']
        return redirect(url_for('user.login'))
    
    elif request.method == 'GET':
        return render_template('user/reset_password/redefinicao-senha.html')

@bp.route('/profile', methods=['GET', 'POST'])
def profile():
    
    dict_user_example = {
            'id_user': 1,
            'username' : 'Mateus Toni Vieira',
            'email' : 'mateustoni04@gmail.com',
            'password' : '12345',
            'cpf_cnpj' : '338.058.828-82',
            'telefone' : '(11)94103-0316',
            'credit_card' : '4723.7623.2130.7436',
        }
        
    list_reservations = [
        {
            'id' : '1',
            'box': 'Box Faria Lima',
            'details': '18 de março de 2022 (4 horas - 13:00 às 17:00)'
        }
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



