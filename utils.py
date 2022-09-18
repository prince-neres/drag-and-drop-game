import json
from flask import Response


def gera_response(status, content, mensage=False):
    body = content
    if(mensage):
        body['mensage'] = mensage
    return Response(json.dumps(body), status=status, mimetype='application/json')
