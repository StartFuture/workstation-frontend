from datetime import datetime
import logging

from flask import render_template, request, redirect, url_for, flash, jsonify, session

#from app import authorization
import functions
import authorization
from box import bp, manager

@bp.route('/', methods=['GET', 'POST'])
@authorization.is_not_auth
def index_box():
    
    if request.method == 'GET':
        profile = dict(session).get('profile', [])
        boxes_get = manager.get_boxes()
        return render_template('box/box.html', boxes=boxes_get, profile=profile)

@bp.route('/search', methods=['GET', 'POST'])
@authorization.is_not_auth
def search_box():
    profile = dict(session).get('profile', [])
    return render_template('box/box-pesquisa.html', profile=profile)


@bp.route('/details/<id_box>', methods=['GET'])
@authorization.is_not_auth
def box_details(id_box):

    profile = dict(session).get('profile', [])
    boxes_get = manager.get_boxes(id_box=id_box)
    street_search_google_maps = manager.process_adress_box(boxes_get, replace_space='%20')
    return render_template('box/box-detalhes.html', boxes=boxes_get, profile=profile, street_search_google_maps=street_search_google_maps)

@bp.route('/confirm', methods=['POST'])
@authorization.is_auth
def box_confirm():

    schedule_infos = request.form.to_dict()
    id_box = schedule_infos['id_box']
    boxes_get = manager.get_boxes(id_box=id_box)

    date_schedule = datetime.strptime(schedule_infos['data'], '%Y-%m-%d').strftime('%d/%m/%Y')

    list_scheduled_times = [value for key, value in schedule_infos.items() if key[:4] == 'time']
    times_show_screen = ', '.join(list_scheduled_times)
    
    qtd_hours = len(list_scheduled_times)
    price_hour_box = boxes_get['preco_hora']
    total_price = str(int(qtd_hours) * float(price_hour_box)).replace('.', ',')
    
    box_name = boxes_get['nome']
    box_complete_adress = manager.process_adress_box(boxes_get)
    
    print(schedule_infos)
    print(boxes_get)
    print('*'*10)
    print(f'''
            date_schedule: {date_schedule}
            list_scheduled_times: {list_scheduled_times}
            times_show_screen: {times_show_screen}
            qtd_hours: {qtd_hours}
            total_price: {total_price}
        '''
    )
    #functions.send_email_password_box(cod='4356', client_email="mateustoni04@gmail.com")
    
    return render_template('box/confirm_schedule.html', date_schedule=date_schedule, times_show_screen=times_show_screen, qtd_hours=qtd_hours, price_hour_box=str(price_hour_box).replace('.', ','), total_price=total_price, box_name=box_name, box_complete_adress=box_complete_adress, status='start')
