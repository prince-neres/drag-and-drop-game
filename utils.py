import json
from flask import Response
from models import Atividade, Categoria, Item


def list_temas():
    temas = Atividade.query.all()
    return temas


def get_tema(id):
    atividade = Atividade.query.filter_by(id=id).first()
    categorias = Categoria.query.filter_by(activity=id)
    items = Item.query.filter_by(activity=id)
    atividade_json = atividade.to_json()
    categorias_json = [categoria.to_json() for categoria in categorias]
    items_json = [item.to_json() for item in items]

    for categoria in categorias_json:
        categoria['items'] = []
        for item in items_json:
            if item['category_id'] == categoria['id']:
                categoria['items'].append(item)

    tema = {
    "atividade": atividade_json,
    "categorias": categorias_json,
    }

    return tema


def gera_response(status, content, mensage=False):
    body = content
    if(mensage):
        body['mensage'] = mensage
    return Response(json.dumps(body), status=status, mimetype='application/json')
