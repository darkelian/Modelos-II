from flask import Blueprint, request, jsonify
from database.database import db
from models.ejercicio import Ejercicio

ejercicios_bp = Blueprint('ejercicios_bp', __name__)


@ejercicios_bp.route('/', methods=['POST'])
def agregar_ejercicio():
    datos = request.get_json()
    nuevo_ejercicio = Ejercicio(enunciado=datos['enunciado'])
    db.session.add(nuevo_ejercicio)
    db.session.commit()
    return jsonify({'mensaje': 'Ejercicio agregado'}), 201


@ejercicios_bp.route('/', methods=['GET'])
def obtener_ejercicios():
    ejercicios = Ejercicio.query.all()
    return jsonify([{'id': ejercicio.id, 'enunciado': ejercicio.enunciado} for ejercicio in ejercicios]), 200


@ejercicios_bp.route('/<int:id>', methods=['PUT'])
def actualizar_ejercicio(id):
    datos = request.get_json()
    ejercicio = Ejercicio.query.get_or_404(id)
    ejercicio.enunciado = datos['enunciado']
    db.session.commit()
    return jsonify({'mensaje': 'Ejercicio actualizado'}), 200


@ejercicios_bp.route('/<int:id>', methods=['DELETE'])
def eliminar_ejercicio(id):
    ejercicio = Ejercicio.query.get_or_404(id)
    db.session.delete(ejercicio)
    db.session.commit()
    return jsonify({'mensaje': 'Ejercicio eliminado'}), 200
