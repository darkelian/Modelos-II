from flask import Blueprint, request, jsonify
from database.database import db
from models.curso import Curso

cursos_bp = Blueprint('cursos_bp', __name__)

@cursos_bp.route('/', methods=['POST'])
def agregar_curso():
    datos = request.get_json()
    nuevo_curso = Curso(nombre=datos['nombre'])
    db.session.add(nuevo_curso)
    db.session.commit()
    return jsonify({'mensaje': 'Curso agregado'}), 201

@cursos_bp.route('/', methods=['GET'])
def obtener_cursos():
    cursos = Curso.query.all()
    return jsonify([{'id': curso.id, 'nombre': curso.nombre} for curso in cursos]), 200

@cursos_bp.route('/<int:id>', methods=['PUT'])
def actualizar_curso(id):
    datos = request.get_json()
    curso = Curso.query.get_or_404(id)
    curso.nombre = datos['nombre']
    db.session.commit()
    return jsonify({'mensaje': 'Curso actualizado'}), 200

@cursos_bp.route('/<int:id>', methods=['DELETE'])
def eliminar_curso(id):
    curso = Curso.query.get_or_404(id)
    db.session.delete(curso)
    db.session.commit()
    return jsonify({'mensaje': 'Curso eliminado'}), 200
