import os
from functools import wraps
from flask import session, redirect, Blueprint, render_template, url_for
import requests

import parameters

def get_credentials_header(server, user, password):
    credentials = {"username": user, "password": password}
    r = requests.post(server + parameters.PATH_LOGIN_API, json=credentials)
    token = r.json()["access_token"]
    headers = {"Authorization": "Bearer {token}".format(token=token)}
    return headers


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "user" not in session:
            # Redirect to Login page here
            return redirect(url_for("user.login"))
        return f(*args, **kwargs)

    return decorated

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