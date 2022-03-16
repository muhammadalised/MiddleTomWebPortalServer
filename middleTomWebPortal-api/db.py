from bson.json_util import dumps, ObjectId
from flask import current_app
from pymongo import MongoClient, DESCENDING
from werkzeug.local import LocalProxy


# Method to Configurate the Connection with the Database
def get_db():
    platzi_db = "mongodb+srv://innovativegxuser:tkeMlLhb4RUmMjRL@cluster0.meo1z.mongodb.net/reportsinnovativepxportal"
    client = MongoClient(platzi_db)
    return client.reportsinnovativepxportal


# Use LocalProxy to read the global db instance with just `db`
db = LocalProxy(get_db)


def test_connection():
    return dumps(db.collection_names())


def collection_stats(collection_nombre):
    return dumps(db.command('collstats', collection_nombre))

# -----------------Carreras-------------------------


def crear_carrera(json):
    return str(db.patients.insert_one(json).inserted_id)


def consultar_carrera_por_id(carrera_id):
    return dumps(db.patients.find_one({'_id': ObjectId(carrera_id)}))


def actualizar_carrera(carrera):
    # Esta funcion solamente actualiza nombre y descripcion de la carrera
    return str(db.patients.update_one({'_id': ObjectId(carrera['_id'])},
                           {'$set': {'nombre': carrera['nombre'], 'descripcion': carrera['descripcion']}})
               .modified_count)


def borrar_carrera_por_id(carrera_id):
    return str(db.patients.delete_one({'_id': ObjectId(carrera_id)}).deleted_count)


# Clase de operadores
def consultar_carreras(skip, limit):
    return dumps(db.patients.find({}).skip(int(skip)).limit(int(limit)))


def agregar_curso(json):
    curso = consultar_curso_por_id_proyeccion(json['id_report'], proyeccion={'nombre': 1})
    return str(db.patients.update_one({'_id': ObjectId(json['id_patient'])}, {'$addToSet': {'cursos': curso}}).modified_count)



def borrar_curso_de_carrera(json):
    return str(db.patients.update_one({'_id': ObjectId(json['id_patient'])}, {'$pull': {'cursos': {'_id': ObjectId(json['id_report'])}}}).modified_count)

# -----------------Cursos-------------------------


def crear_curso(json):
    return str(db.reports.insert_one(json).inserted_id)


def consultar_curso_por_id(id_report):
    return dumps(db.reports.find_one({'_id': ObjectId(id_report)}))


def consultar_cursos(skip, limit):
    return dumps(db.reports.find({}).skip(int(skip)).limit(int(limit)))

def actualizar_curso(report):
    # Esta funcion solamente actualiza nombre, descripcion y clases del curso
    return str('Falta por implementar')


def borrar_curso_por_id(curso_id):
    return str(db.reports.delete_one({'_id': ObjectId(curso_id)}).deleted_count)


def consultar_curso_por_id_proyeccion(id_report, proyeccion=None):
    return db.reports.find_one({'_id': ObjectId(id_report)}, proyeccion)


def consultar_curso_por_nombre(SampleNumber):
    return dumps(db.reports.find({'$text': {'$search':SampleNumber}}))

