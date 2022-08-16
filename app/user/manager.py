import requests
import logging

from flask import url_for, redirect, session

import parameters

def create_user(dict_user):
    
    return requests.post(parameters.PATH_API_BACKEND + parameters.PATH_SIGNUP, json=dict_user)

def update_username(username, last_name):
    token = session['token']
    result = requests.put(parameters.PATH_API_BACKEND + parameters.PATH_UPDATE_USERNAME, headers={'Authorization': f'Bearer {token}'}, json={'name': username, 'last_name' : last_name})

def update_email(value):
    token = session['token']
    result = requests.put(parameters.PATH_API_BACKEND + parameters.PATH_UPDATE_EMAIL, headers={'Authorization': f'Bearer {token}'}, json={'email': value})

def update_cpf_cnpj(value):
    token = session['token']
    result = requests.put(parameters.PATH_API_BACKEND + parameters.PATH_UPDATE_CPF, headers={'Authorization': f'Bearer {token}'}, json={'cpf': value})

def update_telefone(value):
    token = session['token']
    result = requests.put(parameters.PATH_API_BACKEND + parameters.PATH_UPDATE_CELLPHONE, headers={'Authorization': f'Bearer {token}'}, json={'cellphone': value})

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
    
    