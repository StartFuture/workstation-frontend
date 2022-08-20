from flask import render_template, request, redirect, url_for, flash, jsonify, session
import logging

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


@bp.route('/details/<id_box>', methods=['GET', 'POST'])
@authorization.is_not_auth
def box_details(id_box):
    
    if request.method == 'POST':
        
        infos = request.form.to_dict()
        print(infos)
        print('*'*10)
        manager.create_schedule(id_box=id_box, dict_data=infos)

        
        return redirect(url_for('box.box_details', id_box=id_box))

    elif request.method == 'GET':
        profile = dict(session).get('profile', [])
        boxes_get = manager.get_boxes(id_box=id_box)
        cep_search = boxes_get['cep'][:-3] + '-' + boxes_get['cep'][-3:]
        street_search_google_maps = boxes_get['rua'] + str(boxes_get['numero']) +  boxes_get['bairro'] + boxes_get['cidade'] + boxes_get['estado'] + cep_search
        
        return render_template('box/box-detalhes.html', boxes=boxes_get, profile=profile, street_search_google_maps=street_search_google_maps.replace(' ', '%20'))

@bp.route('/confirm', methods=['GET', 'POST'])
@authorization.is_auth
def confirm_box():   
    #functions.send_email_password_box(cod='4356', client_email="mateustoni04@gmail.com")
    return render_template('box/confirmacao-reserva-box.html')
