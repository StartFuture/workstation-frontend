from flask import render_template, request, redirect, url_for, flash, jsonify
from requests import session
import logging

from box import bp

@bp.route('/', methods=['GET', 'POST'])
def index_box():
    boxes = [
                {
                    "cep": "06226-170",
                    "rua": "salvador",
                    "numero": "87",
                    "complemento": "perto d elá",
                    "bairro": "rochdalle",
                    "cidade": "osasco",
                    "estado": "Sao paulo",
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
                    "cep": "06226-170",
                    "rua": "itajai",
                    "numero": "72",
                    "complemento": "perto d elá",
                    "bairro": "aqui mesmo",
                    "cidade": "osasco",
                    "estado": "Sao paulo",
                    "nome": "Biblioteca de Osasco",
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

        return render_template('box/box.html', boxes=boxes)


@bp.route('/search', methods=['GET', 'POST'])
def search_box():    
    return render_template('box/box-pesquisa.html')


@bp.route('/details', methods=['GET', 'POST'])
def detalhes_box():
    if request.method == 'POST':
        
        infos = request.form.to_dict()
        
        logging.warning(infos)
        
        return redirect(url_for('user.login'))

    elif request.method == 'GET':
        
        return render_template('box/box-detalhes.html')

@bp.route('/confirm', methods=['GET', 'POST'])
def confirm_box():    
    return render_template('box/confirmacao-reserva-box.html')
