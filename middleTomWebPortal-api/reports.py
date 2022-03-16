from flask import Blueprint, request, jsonify
from . import db
import json
from sqlalchemy import create_engine
from bson.json_util import dumps, loads

bp = Blueprint('reports', __name__, url_prefix='/reports')

@bp.route('', methods=['GET', 'POST', 'PUT', 'DELETE'])
def cursos_func():
    curso_id = request.args.get('id')
    skip = request.args.get('skip')
    limit = request.args.get('limit')

    request_body = request.get_json()
    if request.method == 'POST':
        # Crear curso
        return jsonify({"_id": db.crear_curso(request_body)})
    elif request.method == 'PUT':
        # Actualizar nombre y descripcion de la carrera
        return jsonify({'updates': db.actualizar_curso(request_body)})
    elif request.method == 'DELETE' and curso_id is not None:
        # Borrar una carrera usando el _id
        return jsonify({'deletes': db.borrar_curso_por_id(curso_id)})
    elif curso_id is not None:
        # Obtener curso por id
        result = db.consultar_curso_por_id(curso_id)
        return jsonify({"report": json.loads(result)})
    else:
        # Get All Reports
        skip = (skip, 0)[skip is None]
        limit = (limit, 10)[limit is None]
        result = db.consultar_cursos(skip, limit)
        return jsonify({'reports': json.loads(result)})


@bp.route('/bySampleNumber', methods=['POST'])
def cursos_por_nombre():
    request_body = request.get_json()
    result = db.consultar_curso_por_nombre(request_body["SampleNumber"])
    return jsonify({"reports": json.loads(result)})


@bp.route('/stats')
def stats_collection():
    return jsonify({"collections": json.loads(db.collection_stats("reports"))})
