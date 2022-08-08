from curses import flash
import requests
import logging
from functools import wraps

from flask import url_for, redirect 


from flask import session

from app import parameters

def get_credential_header(user_login, password_user):
    
    credentials = {
        'user_login': user_login,
        'password_user': password_user
    }
    
    response = requests.get(parameters.PATH_API_BACKEND + '/login', json=credentials)
    
    if response.status_code == 200:
        token = response.json()['access_token']
        headers = {
            'Authorization': 'Bearer ' + token
        }        
        return headers
    else:
        return {'status': 'error', 'message': 'Usuário ou senha inválidos'}, response.status_code
    
def get_user_info(headers):
    response = requests.get(parameters.PATH_API_BACKEND + '/user', headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return {'status': 'error', 'message': 'Usuário ou senha inválidos'}, response.status_code

def logout():
    for key in session.keys():
        session.pop(key)
    return redirect(url_for('main.index'))

def is_logged(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user = dict(session).get('token', None)
        # You would add a check here and usethe user id or something to fetch
        # the other data for that user/check if they exist
        if user:
            return f(*args, **kwargs)
        else:
            flash('Por favor, faça login para acessar essa página')
            return redirect(url_for('user.login'))
    return decorated_function