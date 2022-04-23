from flask import render_template, request, redirect, url_for, flash, jsonify
from requests import session
import logging
import functions

from box import bp

@bp.route('/', methods=['GET', 'POST'])
def index_box():
    boxes = [
                { 
                    "cep": "06226-170",
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
                    "complemento": "perto d elá",
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
                    "cep": "06226-170",
                    "rua": "R. Palestra Itália",
                    "numero": "05005-030",
                    "complemento": "perto d elá",
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
                    "cep": "06226-170",
                    "rua": "Av. Gov Magalhães Barata",
                    "numero": "376",
                    "complemento": "perto d elá",
                    "bairro": "São Brás",
                    "cidade": "Belém",
                    "estado": "PA",
                    "nome": "Espaço Parque Belém",
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
    functions.send_email_password_box(cod='4356', client_email="mateustoni04@gmail.com")
    return render_template('box/confirmacao-reserva-box.html')
