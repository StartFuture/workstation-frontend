from wsgiref import headers
import requests
import logging
from functools import wraps

from flask import url_for, redirect, session

import parameters

def verify_token(token):
    response = requests.get(parameters.PATH_API_BACKEND + parameters.PATH_USER_INFO, headers={'Authorization': 'Bearer ' + token})
    if response.status_code == 200:
        return True
    else:
        return False
    
def verify_token_infos(token):
    response = requests.get(parameters.PATH_API_BACKEND + parameters.PATH_VERIFY_JWT_INFOS, headers={'Authorization': 'Bearer ' + token})
    if response.status_code == 200:
        return response.json()
    else:
        return redirect(url_for('user.login'))

def is_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = dict(session).get('token', None)
        print(f'token: {token}')
        # You would add a check here and usethe user id or something to fetch
        # the other data for that user/check if they exist
        
        if token and verify_token(token):
            
            dict_jwt_infos = verify_token_infos(token=token)
            
            if dict_jwt_infos['two_auth'] == False and dict_jwt_infos['recover_passwd'] == False:
                return f(*args, **kwargs)
            elif dict_jwt_infos['two_auth'] == True:
                # flash('Você já realizou o login com sucesso')
                return redirect(url_for('main.index'))
            elif dict_jwt_infos['recover_passwd'] == True:
                return redirect(url_for('user.recover_passwd'))
            else: # non mapped case
                logging.error(f'Non mapped case: {dict_jwt_infos}')
                logout()
                return redirect(url_for('user.login'))
        
        else:
            # flash('Por favor, faça login para acessar essa página')
            return redirect(url_for('user.login'))
    return decorated_function

def is_auth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = dict(session).get('token', None)
        # You would add a check here and usethe user id or something to fetch
        # the other data for that user/check if they exist
        
        if token:
            
            dict_jwt_infos = verify_token_infos(token=token)
            
            if dict_jwt_infos['two_auth'] == False and dict_jwt_infos['recover_passwd'] == False:
                return redirect(url_for('user.code'))
            elif dict_jwt_infos['two_auth'] == True:
                return f(*args, **kwargs)
            elif dict_jwt_infos['recover_passwd'] == True:
                return redirect(url_for('user.recover_passwd'))
            else: # non mapped case
                logging.error(f'Non mapped case: {dict_jwt_infos}')
                logout()
                return redirect(url_for('user.login'))
        else:
            # flash('Por favor, faça login para acessar essa página')
            return redirect(url_for('user.login'))
    return decorated_function

def is_reset_password(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = dict(session).get('token', None)
        # You would add a check here and usethe user id or something to fetch
        # the other data for that user/check if they exist
        
        if token:
            
            dict_jwt_infos = verify_token_infos(token=token)
            
            if dict_jwt_infos['two_auth'] == False and dict_jwt_infos['recover_passwd'] == False:
                return redirect(url_for('user.code'))
            elif dict_jwt_infos['two_auth'] == True:
                # flash('Você já realizou o login com sucesso')
                return redirect(url_for('main.index'))
            elif dict_jwt_infos['recover_passwd'] == True:
                return f(*args, **kwargs)
            else: # non mapped case
                logging.error(f'Non mapped case: {dict_jwt_infos}')
                logout()
                return redirect(url_for('user.login'))
        else:
            # flash('Por favor, faça login para acessar essa página')
            return redirect(url_for('user.login'))
    return decorated_function

def is_not_auth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = dict(session).get('token', None)
        
        if token:
            
            dict_jwt_infos = verify_token_infos(token=token)
            
            if dict_jwt_infos['two_auth'] == False and dict_jwt_infos['recover_passwd'] == False:
                return redirect(url_for('user.code'))
            
            elif dict_jwt_infos['two_auth'] == True:
                return f(*args, **kwargs)
            
            elif dict_jwt_infos['recover_passwd'] == True:    
                return redirect(url_for('user.recover_passwd'))
            
            else:
                logging.error(f'Non mapped case: {dict_jwt_infos}')
                logout()
                return redirect(url_for('user.login'))
        else:
            return f(*args, **kwargs)
    return decorated_function

def is_not_logged(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = dict(session).get('token', None)
        
        if token:
            
            dict_jwt_infos = verify_token_infos(token=token)
            
            if dict_jwt_infos['two_auth'] == False and dict_jwt_infos['recover_passwd'] == False:
                return redirect(url_for('user.code'))
            
            elif dict_jwt_infos['two_auth'] == True:
                # flash('Você já realizou o login com sucesso')
                return redirect(url_for('main.index'))
            
            elif dict_jwt_infos['recover_passwd'] == True:    
                return redirect(url_for('user.recover_passwd'))
            
            else:
                logging.error(f'Non mapped case: {dict_jwt_infos}')
                logout()
                return redirect(url_for('user.login'))
        else:
            return f(*args, **kwargs)
    return decorated_function

def send_code_two_auth():
    print('send_code_two_auth')
    
    token = dict(session).get('token', None)
    
    if token:
        
        response = requests.post(parameters.PATH_API_BACKEND + parameters.PATH_TWO_FACTOR, headers={'Authorization': f'Bearer {token}'})
        
        if response.status_code == 200:
            
            valid_token = True
            return token, valid_token
        
        else:
            token = None
            valid_token = False
            return token, valid_token
        
    else:
        token = None
        valid_token = False
        return token, valid_token

def get_two_auth_token(code):
    
    token = dict(session).get('token', None)
    
    if token:
        
        two_auth_token = requests.get(parameters.PATH_API_BACKEND + parameters.PATH_TWO_FACTOR, headers={'Authorization': f'Bearer {token}'}, json={'cod_user': code})
    
        print(two_auth_token.content)
        
        if two_auth_token.status_code == 200:
            
            token = two_auth_token.json()['access_token']
            session['token'] = token
        
        elif two_auth_token.status_code == 410: # code expired
            # flash('O código de verificação expirou, por favor, tente novamente')
            logout()
            redirect(url_for('user.login'))
        else:
            pass
            # flash('Código de autenticação inválido')
        

def get_jwt_token(user_login, password_user):
    
    credentials = {
        'user_login': user_login,
        'password_user': password_user
    }
    
    response = requests.get(parameters.PATH_API_BACKEND + parameters.PATH_LOGIN, json=credentials)
    
    if response.status_code == 200:
        token = response.json()['access_token']
        valid_token = True
        return token, valid_token
    
    else:
        token = None
        valid_token = False
        return token, valid_token

def get_credential_header(user_login, password_user):
        
    token, valid_token = get_jwt_token(user_login, password_user)
    
    if valid_token:
        headers = {
            'Authorization': f'Bearer {token}'
        }        
        return headers, True
    else:
        return None, False
    
def get_user_info(headers):
    response = requests.get(parameters.PATH_API_BACKEND + parameters.PATH_USER_INFO, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return {'status': 'error', 'message': 'Usuário ou senha inválidos'}, response.status_code

def logout():
    session.clear()
    
    # here should be a logout request to the backend
    
    # flash('Você foi deslogado com sucesso')
    return redirect(url_for('main.index'))