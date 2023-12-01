from flask import Blueprint, request, jsonify
from database.database import db
from models.maraton import Maraton

maraton_bp = Blueprint('maraton_bp', __name__)


@maraton_bp.route('/', methods=['POST'])
def agregar_maraton():
    datos = request.get_json()
    nuevo_maraton = Maraton(nombre=datos['nombre'])
    db.session.add(nuevo_maraton)
    db.session.commit()

    return jsonify({'mensaje': 'OK'}), 201


@maraton_bp.route('/', methods=['GET'])
def obtener_maratones():
    maratones = Maraton.query.all()
    return jsonify([{
        'id': maraton.id,
        'creado': maraton.creado,
        'actualizado': maraton.actualizado,
        'nombre': maraton.nombre,
    } for maraton in maratones]), 200


@maraton_bp.route('/<int:id>', methods=['PUT'])
def actualizar_maraton(id):
    datos = request.get_json()
    maraton = Maraton.query.get_or_404(id)
    # Actualiza campos si es necesario. Ejemplo:
    # maraton.algun_campo = datos['algun_campo']
    db.session.commit()
    return jsonify({'mensaje': 'Maratón actualizado'}), 200


@maraton_bp.route('/<int:id>', methods=['DELETE'])
def eliminar_maraton(id):
    maraton = Maraton.query.get_or_404(id)
    db.session.delete(maraton)
    db.session.commit()
    return jsonify({'mensaje': 'Maratón eliminado'}), 200
