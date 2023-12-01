from flask import Blueprint, request, jsonify
from database.database import db
from models.grupo_ejercicio import GrupoEjercicio

grupo_ejercicio_bp = Blueprint('grupo_ejercicio_bp', __name__)


@grupo_ejercicio_bp.route('/', methods=['POST'])
def agregar_grupo_ejercicio():
    datos = request.get_json()
    nuevo_grupo_ejercicio = GrupoEjercicio(
        grupo_id=datos['grupo_id'],
        ejercicio_id=datos['ejercicio_id'],
        solucion=datos.get('solucion'),
        duracion_solucion=datos.get('duracion_solucion'),
        maraton_id=datos['maraton_id']
    )
    db.session.add(nuevo_grupo_ejercicio)
    db.session.commit()
    return jsonify({'mensaje': 'Grupo Ejercicio agregado'}), 201


@grupo_ejercicio_bp.route('/', methods=['GET'])
def obtener_grupos_ejercicios():
    grupos_ejercicios = GrupoEjercicio.query.all()
    return jsonify([{
        'grupo_id': ge.grupo_id, 
        'ejercicio_id': ge.ejercicio_id,
        'solucion': ge.solucion,
        'duracion_solucion': ge.duracion_solucion,
        'maraton_id': ge.maraton_id
    } for ge in grupos_ejercicios]), 200


@grupo_ejercicio_bp.route('/<int:grupo_id>/<int:ejercicio_id>', methods=['PUT'])
def actualizar_grupo_ejercicio(grupo_id, ejercicio_id):
    datos = request.get_json()
    grupo_ejercicio = GrupoEjercicio.query.filter_by(grupo_id=grupo_id, ejercicio_id=ejercicio_id).first_or_404()
    grupo_ejercicio.solucion = datos.get('solucion', grupo_ejercicio.solucion)
    grupo_ejercicio.duracion_solucion = datos.get('duracion_solucion', grupo_ejercicio.duracion_solucion)
    db.session.commit()
    return jsonify({'mensaje': 'Grupo Ejercicio actualizado'}), 200


@grupo_ejercicio_bp.route('/<int:grupo_id>/<int:ejercicio_id>', methods=['DELETE'])
def eliminar_grupo_ejercicio(grupo_id, ejercicio_id):
    grupo_ejercicio = GrupoEjercicio.query.filter_by(grupo_id=grupo_id, ejercicio_id=ejercicio_id).first_or_404()
    db.session.delete(grupo_ejercicio)
    db.session.commit()
    return jsonify({'mensaje': 'Grupo Ejercicio eliminado'}), 200
