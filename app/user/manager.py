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

def delete_schedule(dict_json : dict):
    token = session['token']
    list_schedules = eval(dict_json['agendamento'])

    result = requests.delete(parameters.PATH_API_BACKEND + parameters.PATH_DELETE_SCHEDULE, headers={'Authorization': f'Bearer {token}'}, json={'id_box' : dict_json['id_box'], 'date': dict_json['date'], 'list_schedules': [list_schedules]})
    

def get_schedule():
    token = session['token']
    result = requests.get(parameters.PATH_API_BACKEND + parameters.PATH_SHOW_SCHEDULE, headers={'Authorization': f'Bearer {token}'})
    return result.json()

def process_schedules_user(dict_json : dict):
    print(dict_json)
    print('/*/*')
    print(dict_json['list_schedules'])
    list_schedules_processed = []
    for schedule in dict_json['list_schedules']:
    
        day = schedule['data'][:2]
        month = schedule['data'][3:5]
        year = schedule['data'][-4:]

        qtd_hours = len(schedule['used_times'])

        list_times_raw = [time_schedule[:5] for time_schedule in schedule['used_times']]
        list_times_raw = sorted(list_times_raw, key= lambda x: x[:2])
        list_times = ', '.join(list_times_raw)
        word_hour_pt = 'hora' if qtd_hours == 1 else 'horas'

        date_customized = f'{day} de {parameters.DICT_NUMBERS_TO_MONTH[month]} de {year} ({qtd_hours} {word_hour_pt} - {list_times})'
        
        dict_schedule = {}
        dict_schedule['id'] = schedule['id_box']
        dict_schedule['box'] = schedule['nome_box']
        dict_schedule['details'] = date_customized
        dict_schedule['data'] = f'{year}-{month}-{day}'
        dict_schedule['list_times_raw'] = list_times_raw

        list_schedules_processed.append(dict_schedule)
    return list_schedules_processed

    