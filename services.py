from flask import jsonify


def validate_theme(data):
  name = data['name']
  description = data['description']
  categories = data['categories']

  if not data:
    response = jsonify({'error': 'Sem informaçãoes suficientes para criação!'})
    return False, response
  elif not name:
    response = jsonify({'error': 'O nome não pode ficar em branco!'})
    return False, response
  elif not description:
    response = jsonify({'error': 'A descrição não pode ficar em branco!'})
    return False, response
  elif len(categories) < 2:
    response = jsonify({'error': 'Erro temas não podem ter menos de 2 categorias!'})
    return False, response
  elif len(categories) > 10:
    response = jsonify({'error': 'Erro temas não podem ter mais de 10 categorias!'})
    return False, response
  for category in categories:
    if len(category['items']) > 10:
      response = jsonify({'error': 'Erro cateogrias não podem ter mais de 10 items!'})
      return False, response
    elif not category['name']:
      response = jsonify({'error': 'O nome da categoria não pode ficar em branco!'})
      return False, response
    elif len(category['items']) < 1:
      response = jsonify({'error': 'Erro cateogrias não podem ter menos 2 items!'})
      return False, response
    for item in category['items']:
      if not item['name']:
        response = jsonify({'error': 'O nome do item não pode ficar em branco!'})
        return False, response
  return True, {}
