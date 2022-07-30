from unicodedata import category
from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
cors = CORS(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:val44@localhost/jogo'
db = SQLAlchemy(app)

class Atividade(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50))
  description = db.Column(db.String(1000))

  def to_json(self):
    return { 'id': self.id, 'name': self.name, 'description': self.description }

class Categoria(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50))
  description = db.Column(db.String(1000))
  activity = db.Column(db.Integer, db.ForeignKey('atividade.id'))

  def to_json(self):
    return { 'id': self.id, 'name': self.name, 'description': self.description }

class Item(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50))
  description = db.Column(db.String(1000))
  activity = db.Column(db.Integer, db.ForeignKey('atividade.id'))
  category = db.Column(db.Integer, db.ForeignKey('categoria.id'))

  def to_json(self):
    return { 'id': self.id, 'name': self.name, 'description': self.description }


@app.route('/temas', methods=['GET'])
@cross_origin()
def list_temas():
  atividades = Atividade.query.all()
  atividades_json = [atividade.to_json() for atividade in atividades]
  return gera_response(200, atividades_json)

@app.route('/tema/<id>')
@cross_origin()
def get_tema(id):
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


with app.app_context():
    db.create_all()

app.run(debug=True)
