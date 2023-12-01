from flask import Blueprint, request, jsonify
from database.database import db
from models.rol import Rol

rol_bp = Blueprint('rol_bp', __name__)


@rol_bp.route('/', methods=['POST'])
def agregar_rol():
    datos = request.get_json()
    nuevo_rol = Rol(nombre=datos['nombre'])
    db.session.add(nuevo_rol)
    db.session.commit()
    return jsonify({'mensaje': 'Rol agregado'}), 201


@rol_bp.route('/', methods=['GET'])
def obtener_roles():
    roles = Rol.query.all()
    return jsonify([{'id': rol.id, 'nombre': rol.nombre} for rol in roles]), 200


@rol_bp.route('/<int:id>', methods=['PUT'])
def actualizar_rol(id):
    datos = request.get_json()
    rol = Rol.query.get_or_404(id)
    rol.nombre = datos['nombre']
    db.session.commit()
    return jsonify({'mensaje': 'Rol actualizado'}), 200


@rol_bp.route('/<int:id>', methods=['DELETE'])
def eliminar_rol(id):
    rol = Rol.query.get_or_404(id)
    db.session.delete(rol)
    db.session.commit()
    return jsonify({'mensaje': 'Rol eliminado'}), 200
