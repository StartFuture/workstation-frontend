import logging, requests

from flask import render_template, request, redirect, url_for, flash, jsonify, session

from user import bp, manager

import utils, parameters, functions, authorization

@bp.route('/')
def index():
    
    print(session)
    
    token = dict(session).get('token', {})
    if token:
        authorization.get_info_users(token)
    return redirect(url_for('main.index'))


@bp.route('/login', methods=['GET', 'POST'])
@authorization.is_not_logged
def login():

    if request.method == 'POST':

        if 'login' in request.form and 'password' in request.form:
            user_login = request.form['login']
            password_user = request.form['password']
            
            if user_login == '' or password_user == '':
                # flash('Preencha todos os campos!')
                return redirect(url_for('user.login'))
            
            token, valid_token = authorization.get_jwt_token(user_login, password_user)
            
            if valid_token:
            
                session['token'] = token
                
                authorization.send_code_two_auth()
                
                return redirect(url_for('user.code'))
            
            else:
                # flash('Usuário ou senha inválidos!')
                return redirect(url_for('user.login'))
        
        else:
            # flash('Preencha todos os campos!')
            return redirect(url_for('user.login'))
        
    elif request.method == 'GET':
        
        return render_template('user/login/login.html')


@bp.route('/logout')
def logout():
    authorization.logout()
    return redirect(url_for('main.index'))


@bp.route('/code', methods=['GET', 'POST'])
@authorization.is_login
def code():
    
    if request.method == 'POST':
        cod_user = request.form['cod_user']
        
        if cod_user and cod_user.isnumeric and int(cod_user) >= 111111 and int(cod_user) <= 9999999:
            
            authorization.get_two_auth_token(code=cod_user)
            
            return redirect(url_for('main.index'))

    elif request.method == 'GET':
        
        # functions.send_email(cod=dict_code['code'], client_email=dict_code['email'])

        return render_template('user/login/login_autenticacao.html')        

@bp.route('/register', methods=['GET', 'POST'])
@authorization.is_not_logged
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
        "sobrenome": last_name.strip(),
        "data_aniversario": infos["birthday"],
        "sexo": infos["sexo"],
        "telefone": infos["phone"],
        "email": infos["email"],
        "senha": infos["password"],
        "cpf_cnpj": infos["cpf_cnpj"]
        }

        resp = manager.create_user(dict_front_register)
        
        if resp.status_code == 200:
            
            return redirect(url_for('user.login'))
        
        elif resp.status_code == 400:
            
            #flash('user alredy exist')
            return render_template('user/register/cadastro.html')
        
        else:
            
            #flash('erro')
            return render_template('user/register/cadastro.html')
    
    elif request.method == 'GET':
        return render_template('user/register/cadastro.html')
    

@bp.route('/reset/password', methods=['GET', 'POST'])
@authorization.is_not_auth
def reset_password():

    if request.method == 'POST':

        email = dict(request.form).get('email_recover', None)

        if email:
            print(email)

            status = manager.send_reset_password_request(email)

            if status:
                flash('Email enviado com sucesso!, verifique sua caixa de entrada!')
            else:
                flash('Email não encontrado!')
            # flash('Olhe sua caixa de entrada!')
            return redirect(url_for('main.index'))

    elif request.method == 'GET':
        return render_template('user/reset_password/trocar-senha.html')


'''@bp.route('/valid/code', methods=['GET', 'POST'])
def valid_code():
    
    if request.method == 'POST':
        if str(request.form['code_user']) == str('145544'):
            return redirect(url_for('user.change_password'))
    
    elif request.method == 'GET':
        return render_template('user/reset_password/recuperacao-conta.html')'''

@bp.route('/reset_password', methods=['GET'])
@authorization.is_not_auth
def receive_token_password():
    """Endpoint just to receive reset password token

    Returns:
        flask.redirect: redirect to change password endpoint
    """
    
    args = request.args

    token = args.get('token', None)

    if token:
        session['token'] = token

    return redirect(url_for('user.change_password'))

@bp.route('/change/password', methods=['GET', 'POST'])
@authorization.is_reset_password
def change_password():
    
    if request.method == 'POST':
        password = dict(request.form).get('senha_recover', None)

        token = session['token']
        

        if password:
            print(password)
            
            status = manager.reset_password(token, password)

            if status:
                
                # flash('Sua senha foi alterada com sucesso')
                return redirect(url_for('user.logout'))

            else:

                # flash('Erro ao resetar sua senha, por favor tente novamente')
                return redirect(url_for('user.logout'))
        else:
            return redirect(url_for('user.change_password'))

    elif request.method == 'GET':

        return render_template('user/reset_password/redefinicao-senha.html')

@bp.route('/profile', methods=['GET', 'POST'])
@authorization.is_auth
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
                manager.update_username(id_user, value)
            elif key == 'email':
                manager.update_email(id_user, value)
            elif key == 'password':
                manager.update_password(id_user, value)
            elif key == 'cpf_cnpj':
                manager.update_cpf_cnpj(id_user, value)
            elif key == 'telefone':
                manager.update_telefone(id_user, value)
            elif key == 'credit_card':
                manager.update_credit_card(id_user, value)
        
        return redirect(url_for('user.profile'))
    
    elif request.method == 'GET':
        profile = dict(session).get('profile', {})        
        
        dict_user = {
            'id_user': profile['id'],
            'username' : str(profile['nome'] + ' ' + profile['sobrenome']).title(),
            'email' : profile['email'],
            'password' : '******',
            'cpf_cnpj' : '123',
            'telefone' : profile['telefone'],
            'credit_card' : '1234.5678.9012.3456',
        }
        
        return render_template('user/perfil.html', dict_user=dict_user, list_reservations=list_reservations, profile=profile)



