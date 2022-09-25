from flask import render_template
from flask_cors import cross_origin
from configuration import app, db
from models import Atividade, Categoria, Item
from utils import gera_response, list_temas, get_tema


@app.route('/', methods=['GET'])
@cross_origin()
def home():
  temas = list_temas()
  return render_template('index.html', temas=temas)


@app.route('/formulario', methods=['GET'])
@cross_origin()
def form():
  return render_template('formulario.html')


@app.route('/editar/<int:id>', methods=['GET'])
@cross_origin()
def update(id):
  tema = get_tema(id)
  return render_template('edicao.html', tema=tema)


@app.route('/sobre', methods=['GET'])
@cross_origin()
def about():
  return render_template('sobre.html')


@app.route('/tema/<id>', methods=['GET'])
@cross_origin()
def theme(id):
  atividade = Atividade.query.filter_by(id=id).first()
  categorias = Categoria.query.filter_by(activity=id)
  items = Item.query.filter_by(activity=id)
  return render_template('jogo.html', atividade=atividade, categorias=categorias, items=items)


@app.route('/api/theme', methods=['POST'])
def create_theme(theme):
  tema = ''
  return gera_response(200, tema)


with app.app_context():
    db.create_all()

app.run(debug=True)
