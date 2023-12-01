from flask import Blueprint, request, jsonify
from database.database import db
from models.estudiante import Estudiante


estudiantes_bp = Blueprint('estudiantes_bp', __name__)


@estudiantes_bp.route('/', methods=['POST'])
def agregar_estudiante():
    datos = request.get_json()
    nuevo_estudiante = Estudiante(
        carnet=datos['carnet'],
        nombre_completo=datos['nombre_completo'],
        email=datos['email']
    )
    db.session.add(nuevo_estudiante)
    db.session.commit()
    return jsonify({'mensaje': 'Estudiante agregado'}), 201


@estudiantes_bp.route('/', methods=['GET'])
def obtener_estudiantes():
    estudiantes = Estudiante.query.all()
    return jsonify([{'carnet': est.carnet, 'nombre_completo': est.nombre_completo, 'email': est.email} for est in estudiantes]), 200


@estudiantes_bp.route('/<int:carnet>', methods=['PUT'])
def actualizar_estudiante(carnet):
    datos = request.get_json()
    estudiante = Estudiante.query.get_or_404(carnet)
    estudiante.nombre_completo = datos['nombre_completo']
    estudiante.email = datos['email']
    db.session.commit()
    return jsonify({'mensaje': 'Estudiante actualizado'}), 200


@estudiantes_bp.route('/<int:carnet>', methods=['DELETE'])
def eliminar_estudiante(carnet):
    estudiante = Estudiante.query.get_or_404(carnet)
    db.session.delete(estudiante)
    db.session.commit()
    return jsonify({'mensaje': 'Estudiante eliminado'}), 200
