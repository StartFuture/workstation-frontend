import logging

from flask import render_template, request, redirect, url_for, flash, jsonify, session

#from app import authorization
import functions
import authorization
import parameters
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
    box_price_day = str(boxes_get['preco_hora'] * 5).replace('.', ',')
    box_price_hour = str(boxes_get['preco_hora']).replace('.', ',')
    return render_template('box/box-detalhes.html', boxes=boxes_get, profile=profile, street_search_google_maps=street_search_google_maps, box_price_day=box_price_day, box_price_hour=box_price_hour)

@bp.route('/confirm', methods=['GET', 'POST'])
@authorization.is_auth
def box_confirm():

    if request.method == 'GET':

        schedule_infos = request.args.to_dict()

        # # schedule_infos = request.form.to_dict()
        # id_box = schedule_infos['id_box']
        # boxes_get = manager.get_boxes(id_box=id_box)

        # date_schedule = datetime.strptime(schedule_infos['data'], '%Y-%m-%d').strftime('%d/%m/%Y')

        # list_scheduled_times = [value for key, value in schedule_infos.items() if key[:4] == 'time']
        # times_show_screen = ', '.join(list_scheduled_times)
        
        # qtd_hours = len(list_scheduled_times)
        # price_hour_box = boxes_get['preco_hora']
        # total_price = str(int(qtd_hours) * float(price_hour_box)).replace('.', ',')
        
        # box_name = boxes_get['nome']
        # box_complete_adress = manager.process_adress_box(boxes_get)

        id_box, date_schedule, list_scheduled_times, times_show_screen, qtd_hours, price_hour_box, total_price, box_name, box_complete_adress = manager.process_content_confirm_box(schedule_infos)
        
        return render_template(
            'box/confirm_schedule.html',
            date_schedule=date_schedule, 
            times_show_screen=times_show_screen, 
            qtd_hours=qtd_hours, 
            price_hour_box=str(price_hour_box).replace('.', ','), 
            total_price=total_price, 
            box_name=box_name, 
            box_complete_adress=box_complete_adress, 
            status='start',
            id_box=id_box,
            list_scheduled_times=list_scheduled_times
            )

    elif request.method == 'POST':
        print('post')

        schedule_infos = request.form.to_dict()
        
        result, valid = manager.create_schedule(id_box=schedule_infos['id_box'], dict_data=schedule_infos)
        
        if valid:
            status = 'success'
            error_dates = []
            msg_error = parameters.DEFAULT_ERROR_MSG_SCHEDULE
        else:
            error_dates = result['unavailable_times']
            msg_error = result['msg_error_custom']
            status = 'error'

        id_box, date_schedule, list_scheduled_times, times_show_screen, qtd_hours, price_hour_box, total_price, box_name, box_complete_adress = manager.process_content_confirm_box(schedule_infos)

        print(result)
        print(status)
        print(error_dates)
        return render_template(
            'box/confirm_schedule.html',
            date_schedule=date_schedule, 
            times_show_screen=times_show_screen, 
            qtd_hours=qtd_hours, 
            price_hour_box=str(price_hour_box).replace('.', ','), 
            total_price=total_price, 
            box_name=box_name, 
            box_complete_adress=box_complete_adress, 
            status=status,
            id_box=id_box,
            list_scheduled_times=list_scheduled_times,
            error_dates=', '.join(error_dates),
            msg_error=msg_error
            )
