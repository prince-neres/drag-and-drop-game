from flask import Flask, render_template, request, jsonify, redirect, url_for
import database as dbase  
from datetime import datetime
from bson import ObjectId
from theme import Theme

db = dbase.dbConnection()
app = Flask(__name__)


# Lista todos temas
@app.route('/', methods=['GET'])
def home():
    themes = db['themes']
    themes = themes.find()
    return render_template('index.html', temas=themes)


# Template de jogo
@app.route('/tema/<string:id>', methods=['GET'])
def game(id):
    themes = db['themes']
    theme = themes.find_one({"_id": ObjectId(id)})
    categories = theme['categories']
    items = []

    for category in categories:
        for item in category:
            items.append(item)

    return render_template('jogo.html', tema=theme, categories=categories, items=items)


# Formulário para criação de novo tema
@app.route('/formulario', methods=['GET'])
def form():
  return render_template('formulario.html')


# Template para edição de tema
@app.route('/editar/<string:id>', methods=['GET'])
def update(id):
  themes = db['themes']
  theme = themes.find_one({"_id": ObjectId(id)})
  return render_template('edicao.html', tema=theme)


# Template sobre aplicação de desenvolvedores
@app.route('/sobre', methods=['GET'])
def about():
  return render_template('sobre.html')


# Rota para criação de tema
@app.route('/create_theme', methods=['POST'])
def create_theme():
  now = datetime.now()
  themes = db['themes']
  data = request.get_json()
  data['created_date'] = now
  data['updated_date'] = now

  if data:
    themes.insert_one(data)
    resp = jsonify(success=True)
    return resp
  else:
    return notFound()


# Rota para atualização de tema
@app.route('/update_theme/<string:id>', methods=['PUT'])
def update_theme(id):
  data = request.get_json()
  now = datetime.now()
  themes = db.themes

  if data:
    theme = {
      "$set": {
        "name": data['name'],
        "description": data['description'],
        "categories": data['categories'],
        "updated_date": now
      }
    }

    themes.update_one({"_id": ObjectId(id)}, theme)
    resp = jsonify(success=True)
    return resp
  else:
    return notFound()


# Rota para remoção de tema
@app.route('/delete_theme/<string:id>', methods=['DELETE'])
def delete_theme(id):
  themes = db.themes
  theme = themes.find_one({"_id": ObjectId(id)})

  if theme:
    themes.delete_one({"_id": ObjectId(id)})
    resp = jsonify(success=True)
    return resp
  else:
    return notFound()


# Response para erros
@app.errorhandler(404)
def notFound(error=None):
    message ={
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response


if __name__ == '__main__':
    app.run(debug=True, port=3000)
