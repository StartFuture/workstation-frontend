import os
from functools import wraps
from flask import session, redirect, Blueprint, render_template, url_for
import requests

import parameters

from app import parameters

def get_credentials_header(server, user, password):
    credentials = {"username": user, "password": password}
    r = requests.post(server + parameters.PATH_LOGIN_API, json=credentials)
    token = r.json()["access_token"]
    headers = {"Authorization": "Bearer {token}".format(token=token)}

    return headers

