from flask import Blueprint, request, jsonify
from database.database import db
from models.estudiante_curso import EstudianteCurso

estudiante_curso_bp = Blueprint('estudiante_curso_bp', __name__)


@estudiante_curso_bp.route('/', methods=['POST'])
def agregar_estudiante_curso():
    datos = request.get_json()
    nuevo_estudiante_curso = EstudianteCurso(
        estudiante_carnet=datos['estudiante_carnet'],
        curso_id=datos['curso_id']
    )
    db.session.add(nuevo_estudiante_curso)
    db.session.commit()
    return jsonify({'mensaje': 'Estudiante Curso agregado'}), 201


@estudiante_curso_bp.route('/', methods=['GET'])
def obtener_estudiantes_cursos():
    estudiantes_cursos = EstudianteCurso.query.all()
    return jsonify([{
        'estudiante_carnet': ec.estudiante_carnet, 
        'curso_id': ec.curso_id
    } for ec in estudiantes_cursos]), 200


@estudiante_curso_bp.route('/<int:estudiante_carnet>/<int:curso_id>', methods=['PUT'])
def actualizar_estudiante_curso(estudiante_carnet, curso_id):
    datos = request.get_json()
    estudiante_curso = EstudianteCurso.query.filter_by(estudiante_carnet=estudiante_carnet, curso_id=curso_id).first_or_404()
    # Aquí puedes agregar campos adicionales para actualizar si los necesitas
    db.session.commit()
    return jsonify({'mensaje': 'Estudiante Curso actualizado'}), 200


@estudiante_curso_bp.route('/<int:estudiante_carnet>/<int:curso_id>', methods=['DELETE'])
def eliminar_estudiante_curso(estudiante_carnet, curso_id):
    estudiante_curso = EstudianteCurso.query.filter_by(estudiante_carnet=estudiante_carnet, curso_id=curso_id).first_or_404()
    db.session.delete(estudiante_curso)
    db.session.commit()
    return jsonify({'mensaje': 'Estudiante Curso eliminado'}), 200
