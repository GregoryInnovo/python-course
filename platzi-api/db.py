from bson.json_util import dumps, ObjectId
from flask import current_app
from pymongo import MongoClient, DESCENDING
from werkzeug.local import LocalProxy


# Este método se encarga de configurar la conexión con la base de datos
def get_db():
    MONGO_URI = current_app.config['MONGO_URI']
    client = MongoClient(MONGO_URI)
    db = client['test']
    return db


# Use LocalProxy to read the global db instance with just `db`
db = LocalProxy(get_db)


def test_connection():
    print(db.collection_names())
    return 1
    # return dumps(db.collection_names())


def collection_stats(collection_nombre):
    return dumps(db.command('collstats', collection_nombre))

# -----------------Carreras-------------------------


def crear_carrera(json):
    collection = db['carreras']
    return str(collection.insert_one(json).inserted_id)


def consultar_carrera_por_id(carrera_id):
    collection = db['carreras']
    # dumps convert BJSON to JSON
    return dumps(collection.find_one({'_id': ObjectId(carrera_id)}))


def actualizar_carrera(carrera):
    # Esta funcion solamente actualiza nombre y descripcion de la carrera
    collection = db['carreras']
    return collection.update_one({'_id': ObjectId(carrera['_id'])}, {'$set':{'nombre': carrera['nombre'],'descripcion': carrera['descripcion'] }}).modified_count


def borrar_carrera_por_id(carrera_id):
    collection = db['carreras']
    return str(collection.delete_one({ '_id': ObjectId(carrera_id)}))


# Clase de operadores
def consultar_carreras(skip, limit):
    return dumps(db.carreras.find({}).skip(int(skip)).limit(int(limit)))


def agregar_curso(json):
    curso = consultar_curso_por_id_proyeccion(json['id_curso'], proyeccion={'nombre': 1})
    collection = db['carreras']
    return str(collection.update_one({'_id': ObjectId(json['id_carrera'])}, {'$addToSet': {
        'cursos': curso
    }}).modified_count)


def borrar_curso_de_carrera(json):
    collection = db['carreras']
    return str(collection.update_one({'_id': ObjectId(json['id_carrera'])}, 
    {
        '$pull': {
            'cursos': {'_id': ObjectId(json['id_curso'])}
        }
    }).modified_count)

# -----------------Cursos-------------------------


def crear_curso(json):
    collection = db['cursos']
    return str(collection.insert_one(json).inserted_id)


def consultar_curso_por_id(id_curso):
    collection = db['cursos']
    return dumps(collection.find_one({'_id': ObjectId(id_curso)}))


def actualizar_curso(curso):
    # Esta funcion solamente actualiza nombre, descripcion y clases del curso
    collection = db['cursos']
    return str(collection.update_one({'_id': ObjectId(curso['_id'])}, {
        '$set': {
            'nombre': curso['nombre'], 
            'descripcion': curso['descripcion'],
            'clases': curso['clases']
        }
    }).modified_count)


def borrar_curso_por_id(curso_id):
    collection = db['cursos']
    return str(collection.delete_one({'_id': ObjectId(curso_id)}).deleted_count)


def consultar_curso_por_id_proyeccion(id_curso, proyeccion=None):
    collection = db['cursos']
    return collection.find_one({'_id': ObjectId(id_curso)}, proyeccion)


def consultar_curso_por_nombre(nombre):
    collection = db['cursos']
    return dumps(collection.find({'$text': {
        '$search': nombre
    }}))

