import requests
import logging

from flask import url_for, redirect, session

import parameters

def get_boxes(id_box : int = None):
    if id_box:
        result = requests.get(parameters.PATH_API_BACKEND + parameters.PATH_GET_BOX, json={'id': id_box})
    else:
        result = requests.get(parameters.PATH_API_BACKEND + parameters.PATH_GET_BOX)

    if result.status_code == 200:
        return result.json()
    else:
        logging.error(f'Request error app/box/manager.py - get_boxes, returns {result.content}, with status: {result.status_code}')

def create_schedule(id_box, dict_data):
    
    date_selected = dict_data['data']
    list_scheduled_times = [value for key, value in dict_data.items() if key[:4] == 'time']

    token = dict(session).get('token', None)
    
    result = requests.post(
        parameters.PATH_API_BACKEND + parameters.PATH_CREATE_SCHEDULE,
        headers={'Authorization': 'Bearer ' + token},
        json={
            'id_box': id_box, 
            'date_schedule': date_selected, 
            'array_schedule_times': list_scheduled_times
            }
        )

    if result.status_code == 200:
        return result.json()
    else:
        logging.error(f'Request error app/box/manager.py - create_schedule, returns {result.content}, with status: {result.status_code}')