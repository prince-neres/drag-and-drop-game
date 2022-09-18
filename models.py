from configuration import db


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
