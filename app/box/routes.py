from flask import render_template, request, redirect, url_for, flash, jsonify

from box import bp

@bp.route('/')
def index_box():
    return render_template('box/box.html')


@bp.route('/search', methods=['GET', 'POST'])
def search_box():    
    return render_template('box/box-pesquisa.html')


@bp.route('/details', methods=['GET', 'POST'])
def detalhes_box():    
    return render_template('box/box-detalhes.html')


@bp.route('/confirm', methods=['GET', 'POST'])
def confirm_box():    
    return render_template('box/confirmacao-reserva-box-faria.html')
