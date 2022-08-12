import requests
import logging

from flask import url_for, redirect, session

import parameters

def create_user(dict_user):
    
    return requests.post(parameters.PATH_API_BACKEND + parameters.PATH_SIGNUP, json=dict_user)

def update_username(id_user, value):
    pass

def update_email(id_user, value):
    pass

def update_password(id_user, value):
    pass

def update_cpf_cnpj(id_user, value):
    pass

def update_telefone(id_user, value):
    pass

def update_credit_card(id_user, value):
    pass

def send_reset_password_request(email):
    response = requests.post(parameters.PATH_API_BACKEND + parameters.PATH_PASSWORD_RESET, json={'email': email})
    if response.status_code == 200:
        return True
    else:
        return False

def reset_password(token, password):
    response = requests.post(parameters.PATH_API_BACKEND + parameters.PATH_NEW_PASSWORD, headers={'Authorization': f'Bearer {token}'}, json={'password': password})
    
    print(response.content)
    print(response.status_code)
    if response.status_code == 200:
        return True
    else:
        return False
    
    