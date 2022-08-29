import json
from flask import Response, render_template
from app import app, Atividade, Categoria, Item
from flask_cors import CORS, cross_origin


cors = CORS(app)


@app.route('/', methods=['GET'])
@cross_origin()
def home():
  temas = Atividade.query.all()
  return render_template('index.html', temas=temas)


@app.route('/formulario', methods=['GET'])
@cross_origin()
def form():
  return render_template('formulario.html')


@app.route('/sobre', methods=['GET'])
@cross_origin()
def about():
  return render_template('sobre.html')


@app.route('/tema/<id>')
@cross_origin()
def theme(id):
  atividade = Atividade.query.filter_by(id=id).first()
  categorias = Categoria.query.filter_by(activity=id)
  items = Item.query.filter_by(activity=id)
  return render_template('jogo.html', atividade=atividade, categorias=categorias, items=items)


@app.route('/api/theme/<id>')
def get_theme(id):
  atividade = Atividade.query.filter_by(id=id).first()
  categorias = Categoria.query.filter_by(activity=id)
  items = Item.query.filter_by(activity=id)
  atividade_json = atividade.to_json()
  categorias_json = [categoria.to_json() for categoria in categorias]
  items_json = [item.to_json() for item in items]
  tema = {
    "atividade": atividade_json,
    "categorias": categorias_json,
    "items": items_json
  }
  return gera_response(200, tema)


def gera_response(status, content, mensage=False):
    body = content
    if(mensage):
        body['mensage'] = mensage
    return Response(json.dumps(body), status=status, mimetype='application/json')