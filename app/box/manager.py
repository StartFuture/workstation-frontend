import requests
import logging

from flask import url_for, redirect, session

import parameters

def get_all_boxes():
    result = requests.get(parameters.PATH_API_BACKEND + parameters.PATH_GET_ALL_BOX)
    if result.status_code == 200:
        return result.json()
    else:
        logging.error(f'Request error app/box/manager.py - get_all_boxes, returns {result.content}')