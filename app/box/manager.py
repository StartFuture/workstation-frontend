import requests
import logging
from datetime import datetime

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

def process_adress_box(boxes_get, replace_space=' ') -> str:
    cep_search = boxes_get['cep'][:-3] + '-' + boxes_get['cep'][-3:]
    adress_box = boxes_get['rua'] + ', ' + str(boxes_get['numero']) + ' - ' + boxes_get['bairro'] + ', ' + boxes_get['cidade'] + ' - ' + boxes_get['estado'] + ', ' + cep_search
    adress_box = adress_box.replace(' ', replace_space)
    return adress_box

def process_content_confirm_box(schedule_infos):
    id_box = schedule_infos['id_box']
    boxes_get = get_boxes(id_box=id_box)

    if '-' in schedule_infos['data']:
        date_schedule = datetime.strptime(schedule_infos['data'], '%Y-%m-%d').strftime('%d/%m/%Y')
    else:
        date_schedule = schedule_infos['data']
    list_scheduled_times = [value for key, value in schedule_infos.items() if key[:4] == 'time']
    times_show_screen = ', '.join(list_scheduled_times)
    
    qtd_hours = len(list_scheduled_times)
    price_hour_box = boxes_get['preco_hora']
    total_price = str(int(qtd_hours) * float(price_hour_box)).replace('.', ',')
    
    box_name = boxes_get['nome']
    box_complete_adress = process_adress_box(boxes_get)

    return id_box, date_schedule, list_scheduled_times, times_show_screen, qtd_hours, price_hour_box, total_price, box_name, box_complete_adress

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
            'array_schedule_times': [list_scheduled_times]
            }
        )

    print('status')

    if result.status_code == 200:
        valid_return = True
        print(result.json())
        return result.json(), valid_return
    
    elif result.status_code == 400:
        valid_return = False
        logging.error(f'Request error app/box/manager.py - create_schedule, returns {result.content}, with status: {result.status_code}')
        return result.json(), valid_return
    
    elif result.status_code == 410:
        valid_return = False
        logging.error(f'Request error app/box/manager.py - create_schedule, returns {result.content}, with status: {result.status_code}')
        return result.json(), valid_return
    
    else:
        valid_return = False
        logging.error(f'Request error app/box/manager.py - create_schedule, returns {result.content}, with status: {result.status_code}')
        return result.json(), valid_return