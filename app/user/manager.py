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
