from app import db

class Atividade(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50))
  description = db.Column(db.String(1000))

  def to_json(self):
    return { 'id': self.id, 'name': self.name, 'description': self.description }
