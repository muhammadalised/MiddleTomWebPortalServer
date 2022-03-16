from flask import Blueprint, request, jsonify
from . import db
import json

bp = Blueprint('patients', __name__, url_prefix='/patients')


@bp.route('', methods=['GET', 'POST', 'PUT', 'DELETE'])
def carreras_func():
    carrera_id = request.args.get('id')
    skip = request.args.get('skip')
    limit = request.args.get('limit')

    request_body = request.get_json()
    if request.method == 'POST':
        # Create patient of LIMS
        return jsonify({'_id': db.crear_carrera(request_body)})
    elif request.method == 'PUT':
        # Actualizar nombre y descripcion de la carrera
        return jsonify({'updates': db.actualizar_carrera(request_body)})
    elif request.method == 'DELETE' and carrera_id is not None:
        # Delete patient using _id
        return jsonify({'deletes': db.borrar_carrera_por_id(carrera_id)})
    elif carrera_id is not None:
        # Get patients by _id
        result = db.consultar_carrera_por_id(carrera_id)
        return jsonify({'patient': json.loads(result)})
    else:
        # Get All Patients
        skip = (skip, 0)[skip is None]
        limit = (limit, 10)[limit is None]
        result = db.consultar_carreras(skip, limit)
        return jsonify({'patients': json.loads(result)})


@bp.route('/add-report', methods=['PUT', 'DELETE'])
def agregar_curso():
    request_body = request.get_json()
    if request.method == 'PUT':
        return jsonify({'updates': json.loads(db.agregar_curso(request_body))})
    elif request.method == 'DELETE':
        return jsonify({'deletes': json.loads(db.borrar_curso_de_carrera(request_body))})


@bp.route('/test')
def test_connection():
    return jsonify({'collections': json.loads(db.test_connection())})
