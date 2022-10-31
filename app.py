from flask import Flask, render_template, request, jsonify
import database as dbase  
from datetime import datetime
from bson import ObjectId
from random import shuffle

db = dbase.dbConnection()
coll_themes = db['themes']
app = Flask(__name__)


# Lista todos temas
@app.route('/', methods=['GET'])
def home():
    try:
        themes = coll_themes.find()
        return render_template('index.html', temas=themes)
    except Exception as e:
        response = jsonify({"error": f'Erro ao encontrar temas: {e}!'})
        return response


# Template de jogo
@app.route('/tema/<string:id>', methods=['GET'])
def game(id):
    theme = coll_themes.find_one({"_id": ObjectId(id)})

    if theme:
        categories = theme['categories']
        items = []

        for category in categories:
            for item in category['items']:
                items.append(item)
        shuffle(items)

        return render_template('jogo.html', tema=theme, categories=categories, items=items)
    else:
        response = jsonify({"error": "Tema não encontrado!"})
        return response


# Formulário para criação de novo tema
@app.route('/formulario', methods=['GET'])
def form():
    return render_template('formulario.html')


# Template para edição de tema
@app.route('/editar/<string:id>', methods=['GET'])
def update(id):
    theme = coll_themes.find_one({"_id": ObjectId(id)})

    if theme:
        return render_template('edicao.html', tema=theme)
    else:
        response = jsonify({"error": "Tema não encontrado!"})
        return response


# Template sobre aplicação de desenvolvedores
@app.route('/sobre', methods=['GET'])
def about():
    return render_template('sobre.html')


# Rota para criação de tema
@app.route('/create_theme', methods=['POST'])
def create_theme():
    now = datetime.now()
    data = request.get_json()

    if data:
        data['created_date'] = now
        data['updated_date'] = now
      
        try:
            coll_themes.insert_one(data)
            response = jsonify({"success": f'Tema {data["name"]}criado com sucesso!'})
            return response
        except Exception as e:
            response = jsonify({"error": f'Erro ao tentar criar tema: {e}!'})
            return response

    else:
        response = jsonify({"error": "Sem informaçãoes suficientes para criação!"})
        return response


# Rota para atualização de tema
@app.route('/update_theme/<string:id>', methods=['PUT'])
def update_theme(id):
    data = request.get_json()
    now = datetime.now()

    if data:
        theme = {
          "$set": {
            "name": data['name'],
            "description": data['description'],
            "categories": data['categories'],
            "updated_date": now
          }
        }

        try:
            coll_themes.update_one({"_id": ObjectId(id)}, theme)
            response = jsonify({"success": "Tema atualizado com sucesso!"})
            return response
        except Exception as e:
            response = jsonify({"error": f'erro ao tentar editar tema: {e}!'})
            return response

    else:
        response = jsonify({"error": "Sem dados para alterar!"})
        return response


# Rota para remoção de tema
@app.route('/delete_theme/<string:id>', methods=['DELETE'])
def delete_theme(id):
    theme = coll_themes.find_one({"_id": ObjectId(id)})

    if theme:
        coll_themes.delete_one({"_id": ObjectId(id)})
        response = jsonify({"success": "Tema deletado com sucesso!"})
        return response

    else:
        response = jsonify({"error": "Tema não foi encontrado!"})
        return response


if __name__ == '__main__':
    app.run(debug=True, port=3000)
