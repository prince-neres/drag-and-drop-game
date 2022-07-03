from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:val44@localhost/projeto'
db = SQLAlchemy(app)

@app.route('/atividades', methods=['GET'])
def list_atividades():
  atividades = Atividade.query.all()
  atividades_json = [atividades.to_json() for atividade in atividades]
  return gera_response(200, 'atividades', atividades_json)

@app.route('/atividade/<id>')
def get_atividade(id):
  atividade = Atividade.query.filter_by(id=id).first()
  ativideade_json = atividade.to_json()
  return gera_response(200, 'atividade', ativideade_json)

@app.route('/atividade', methods=['POST'])
def create_atividade():
    body = request.get_json()
    try:
        atividade =Atividade(name=body['name'], description= body['description'])
        db.session.add(atividade)
        db.session.commit()
        return gera_response(201, 'atividade', atividade.to_json(), 'Criada com sucesso')
    except Exception as e:
        print('Erro', e)
        return gera_response(400, 'atividade', {}, 'Erro ao cadastrar')

@app.route('/atividade/<id>', methods=['PUT'])
def update_atividade(id):
    atividade =Atividade.query.filter_by(id=id).first()
    body = request.get_json()
    try:
        if('name' in body):
            atividade.name = body['atividade']
        if('description' in body):
            atividade.email = body['description']
        db.session.add(atividade)
        db.session.commit()
        return gera_response(200, 'atividade', atividade.to_json(), 'Atualizada com sucesso')
    except Exception as e:
        print('Erro', e)
        return gera_response(400, 'atividade', {}, 'Erro ao atualizar')

@app.route('/atividade/<id>', methods=['DELETE'])
def delete_atividade(id):
    atividade =Atividade.query.filter_by(id=id).first()
    try:
        db.session.delete(atividade)
        db.session.commit()
        return gera_response(200, 'atividade', atividade.to_json(), 'Deletada com sucesso')
    except Exception as e:
        print('Erro', e)
        return gera_response(400, 'atividade', {}, 'Erro ao deletar')

def gera_response(status, name_content, content, mensage=False):
    body = {}
    body[name_content] = content
    if(mensage):
        body['mensage'] = mensage
    return Response(json.dumps(body), status=status, mimetype='application/json')

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

app.run(debug=True)
