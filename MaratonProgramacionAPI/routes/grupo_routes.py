from flask import Blueprint, request, jsonify
from database.database import db
from models.grupo import Grupo
from models.maraton import Maraton
from models.maraton_grupo import MaratonGrupo
from models.estudiante import Estudiante
from models.estudiante_curso import EstudianteCurso

grupo_bp = Blueprint('grupo_bp', __name__)


@grupo_bp.route('/', methods=['POST'])
def agregar_grupo():
    datos = request.get_json()
    nuevo_grupo = Grupo(
        nombre=datos['nombreGrupo'],
        categoria_id=datos['categoria_id']
    )
    db.session.add(nuevo_grupo)
    db.session.commit()

    grupo_id = nuevo_grupo.id

    maraton_grupo = MaratonGrupo(
        maraton_id=datos['maraton_id'],
        grupo_id=grupo_id
    )
    db.session.add(maraton_grupo)
    db.session.commit()

    estudiantes = datos['estudiantes']

    for estudiante in estudiantes:
        nuevo_estudiante = Estudiante(
            carnet=estudiante['carnet'],
            nombre_completo=estudiante['nombre'],
            email=estudiante['correo']
        )
        db.session.add(nuevo_estudiante)
        db.session.commit()

        cursos = estudiante['cursos']

        for curso in cursos:
            nuevo_estudiante_grupo = EstudianteCurso(
                estudiante_carnet=estudiante['carnet'],
                curso_id=curso
            )
            db.session.add(nuevo_estudiante_grupo)
            db.session.commit()
    
    return jsonify({'mensaje': 'Grupo agregado'}), 201


@grupo_bp.route('/', methods=['GET'])
def obtener_grupos():
    grupos = Grupo.query.all()
    return jsonify([{
        'id': grupo.id, 
        'nombre': grupo.nombre, 
        'categoria_id': grupo.categoria_id
    } for grupo in grupos]), 200


@grupo_bp.route('/<int:id>', methods=['PUT'])
def actualizar_grupo(id):
    datos = request.get_json()
    grupo = Grupo.query.get_or_404(id)
    grupo.nombre = datos['nombre']
    grupo.categoria_id = datos['categoria_id']
    db.session.commit()
    return jsonify({'mensaje': 'Grupo actualizado'}), 200


@grupo_bp.route('/<int:id>', methods=['DELETE'])
def eliminar_grupo(id):
    grupo = Grupo.query.get_or_404(id)
    db.session.delete(grupo)
    db.session.commit()
    return jsonify({'mensaje': 'Grupo eliminado'}), 200


@grupo_bp.route('/existe-grupo', methods=['GET'])
def existe_grupo():
    # Existe grupo por nombre
    nombre = request.args.get('nombre')
    grupo = Grupo.query.filter_by(nombre=nombre).first()
    return jsonify({'existe': grupo is not None}), 200
