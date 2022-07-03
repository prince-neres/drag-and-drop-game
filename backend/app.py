from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import models
import json

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:val44@localhost/jogo'

db = SQLAlchemy(app)

@app.route('/atividades', methods=['GET'])
def list_atividades():
  atividades = models.Atividade.query.all()
  atividades_json = [atividades.to_json() for atividade in atividades]
  return Response(json.dumps(atividades_json))

if __name__ == "__main__":
    app.run(debug=True)