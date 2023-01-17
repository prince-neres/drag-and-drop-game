from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import database as dbase
from services import validate_theme
from datetime import datetime
from bson import ObjectId
from random import shuffle

db = dbase.dbConnection()
coll_themes = db['themes']
coll_scores = db['scores']
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Lista todos temas
@app.route('/', methods=['GET'])
def home():
    try:
        themes = coll_themes.find()
        return render_template('index.html', temas=themes)
    except Exception as e:
        response = jsonify({'error': f'Erro ao encontrar temas: {e}!'})
        return response


# Template de jogo
@app.route('/tema/<string:id>', methods=['GET'])
def game(id):
    theme = coll_themes.find_one({'_id': ObjectId(id)})
    find_record = coll_scores.find({'theme_id':str(id)}).sort('final_score', -1).limit(1)
    record = [record for record in find_record]
    record = record[0] if record else 0

    if theme:
        categories = theme['categories']
        items = []

        for category in categories:
            for item in category['items']:
                item['category'] = category['name']
                items.append(item)

        return render_template('jogo.html', tema=theme, categories=categories, items=items, record=record)
    else:
        response = jsonify({'error': 'Tema não encontrado!'})
        return response


# Templates para criação e edição de tema
@app.route('/formulario/<string:id>', methods=['GET'])
def form(id):
    if id == 'novo':
        return render_template('formulario.html')
    else:
        theme = coll_themes.find_one({'_id': ObjectId(id)})

        if theme:
            return render_template('edicao.html', tema=theme)
        else:
            response = jsonify({'error': 'Tema não encontrado!'})
            return response


# Template sobre aplicação de desenvolvedores
@app.route('/sobre', methods=['GET'])
def about():
    return render_template('sobre.html')


# Rota para criação de tema
@app.route('/create_theme', methods=['POST'])
@cross_origin()
def create_theme():
    now = datetime.now()
    data = request.get_json()
    validate, response = validate_theme(data)

    if validate:
        data['created_date'] = now
        data['updated_date'] = now
        try:
            coll_themes.insert_one(data)
            response = jsonify({'success': f'Tema {data["name"]} criado com sucesso!'})
            return response
        except Exception as e:
            response = jsonify({'error': f'Erro ao tentar criar tema: {e}!'})
            return response
    else:
        return response


# Rota para atualização de tema
@app.route('/update_theme/<string:id>', methods=['PUT'])
@cross_origin()
def update_theme(id):
    data = request.get_json()
    now = datetime.now()
    validate, response = validate_theme(data)
    password = data['password'] if 'password' in data else None 

    if validate:
        theme = {
          '$set': {
            'name': data['name'],
            'description': data['description'],
            'categories': data['categories'],
            'updated_date': now,
            'private': data['private'],
            'password': password
          }
        }
        try:
            coll_themes.update_one({'_id': ObjectId(id)}, theme)
            response = jsonify({'success': 'Tema atualizado com sucesso!'})
            return response
        except Exception as e:
            response = jsonify({'error': f'erro ao tentar editar tema: {e}!'})
            return response
    else:
        return response


# Rota para remoção de tema
@app.route('/delete_theme/<string:id>', methods=['DELETE'])
@cross_origin()
def delete_theme(id):
    theme = coll_themes.find_one({'_id': ObjectId(id)})

    if theme:
        coll_themes.delete_one({'_id': ObjectId(id)})
        response = jsonify({'success': 'Tema deletado com sucesso!'})
        return response
    else:
        response = jsonify({'error': 'Tema não foi encontrado!'})
        return response


# Rota para salvar pontuação
@app.route('/save_score', methods=['POST'])
@cross_origin()
def save_score():
    now = datetime.now()
    data = request.get_json()

    if data:
        data['date'] = now
        data['final_score'] = data['score'] + data['time'] - data['mistakes']

        try:
            coll_scores.insert_one(data)
            response = jsonify({'success': f'Pontuação salva com sucesso!'})
            return response
        except Exception as e:
            response = jsonify({'error': f'Erro ao salvar pontuação: {e}!'})
            return response
    else:
        response = jsonify({'error': 'Sem informaçãoes suficientes para salvar!'})
        return response


if __name__ == '__main__':
    app.run(debug=True)
