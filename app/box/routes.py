from flask import render_template, request, redirect, url_for, flash, jsonify, session
import logging

#from app import authorization
import functions
import authorization
from box import bp, manager

@bp.route('/', methods=['GET', 'POST'])
@authorization.is_not_auth
def index_box():
    boxes = [
                { 
                    "cep": "01452-000",
                    "rua": "Av. Brg. Faria Lima",
                    "numero": "2705",
                    "complemento": "Próximo ao museu",
                    "bairro": "Jardim Paulistano",
                    "cidade": "São Paulo",
                    "estado": "SP",
                    "nome": "Espaço Faria Lima",
                    "preco_hora": "100",
                    "descricao": """
                                Muito mais que uma sala de
                                reunião, um espaço para fechar 
                                negócios importantes e ter grandes 
                                ideias. Capacidade para até 12 
                                pessoas.
                                """
                },
                {
                    "cep": "30160-000",
                    "rua": "Praça Rui Barbosa",
                    "numero": "600",
                    "complemento": "ao lado do hospital",
                    "bairro": "Centro",
                    "cidade": "Belo Horizonte",
                    "estado": "MG",
                    "nome": "Espaço BH",
                    "preco_hora": "100",
                    "descricao": """
                                Muito mais que uma sala de
                                reunião, um espaço para fechar 
                                negócios importantes e ter grandes 
                                ideias. Capacidade para até 12 
                                pessoas.
                                """
                },
                {
                    "cep": "05005-001",
                    "rua": "R. Palestra Itália",
                    "numero": "147",
                    "complemento": "predio B",
                    "bairro": "Centro",
                    "cidade": "Perdizes",
                    "estado": "SP",
                    "nome": "Espaço Bourbom",
                    "preco_hora": "100",
                    "descricao": """
                                Muito mais que uma sala de
                                reunião, um espaço para fechar 
                                negócios importantes e ter grandes 
                                ideias. Capacidade para até 12 
                                pessoas.
                                """
                },
                
                {
                    "cep": "06093-010",
                    "rua": "Av. Gov Magalhães Barata",
                    "numero": "260",
                    "complemento": "2 andar",
                    "bairro": "São Brás",
                    "cidade": "Belém",
                    "estado": "PA",
                    "nome": "Espaço Biblioteca de Osasco",
                    "preco_hora": "100",
                    "descricao": """
                                Muito mais que uma sala de
                                reunião, um espaço para fechar 
                                negócios importantes e ter grandes 
                                ideias. Capacidade para até 12 
                                pessoas.
                                """
                },
                {
                    "cep": "01311-923",
                    "rua": "av paulista",
                    "numero": "1313",
                    "complemento": "proximo a lanchonete x",
                    "bairro": "aqui mesmo",
                    "cidade": "osasco",
                    "estado": "Sao paulo",
                    "nome": "Espaço Paulista",
                    "preco_hora": "200",
                    "descricao": """
                                Muito mais que uma sala de
                                reunião, um espaço para fechar 
                                negócios importantes e ter grandes 
                                ideias. Capacidade para até 12 
                                pessoas.
                                """
                }
            ]
    
    if request.method == 'GET':
        profile = dict(session).get('profile', [])
        boxes_get = manager.get_all_boxes()
        print(boxes_get)
        return render_template('box/box.html', boxes=boxes_get, profile=profile)


@bp.route('/search', methods=['GET', 'POST'])
@authorization.is_not_auth
def search_box():
    profile = dict(session).get('profile', [])
    return render_template('box/box-pesquisa.html', profile=profile)

@bp.route('/create', methods=['POST'])
@authorization.is_not_auth
def create_box():
    profile = dict(session).get('profile', [])
    return {}

@bp.route('/update', methods=['PUT'])
@authorization.is_not_auth
def update_box():
    profile = dict(session).get('profile', [])
    return {}

@bp.route('/delete', methods=['DELETE'])
@authorization.is_not_auth
def delete_box():
    profile = dict(session).get('profile', [])
    return {}

@bp.route('/details', methods=['GET', 'POST'])
@authorization.is_not_auth
def detalhes_box():
    if request.method == 'POST':
        
        infos = request.form.to_dict()
        
        logging.warning(infos)
        
        return redirect(url_for('user.login'))

    elif request.method == 'GET':
        profile = dict(session).get('profile', [])
        return render_template('box/box-detalhes.html', profile=profile)

@bp.route('/confirm', methods=['GET', 'POST'])
@authorization.is_auth
def confirm_box():   
    #functions.send_email_password_box(cod='4356', client_email="mateustoni04@gmail.com")
    return render_template('box/confirmacao-reserva-box.html')
