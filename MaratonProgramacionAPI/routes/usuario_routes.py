from flask import Blueprint, request, jsonify
from database.database import db
from models.usuario import Usuario

usuario_bp = Blueprint('usuario_bp', __name__)


@usuario_bp.route('/', methods=['POST'])
def agregar_usuario():
    datos = request.get_json()
    nuevo_usuario = Usuario(email=datos['email'], clave=datos['clave'], rol_id=datos['rol_id'])
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify({'mensaje': 'Usuario agregado'}), 201


@usuario_bp.route('/', methods=['GET'])
def obtener_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([{'email': usuario.email, 'rol_id': usuario.rol_id} for usuario in usuarios]), 200


@usuario_bp.route('/<string:email>', methods=['PUT'])
def actualizar_usuario(email):
    datos = request.get_json()
    usuario = Usuario.query.get_or_404(email)
    usuario.clave = datos['clave']
    usuario.rol_id = datos['rol_id']
    db.session.commit()
    return jsonify({'mensaje': 'Usuario actualizado'}), 200


@usuario_bp.route('/<string:email>', methods=['DELETE'])
def eliminar_usuario(email):
    usuario = Usuario.query.get_or_404(email)
    db.session.delete(usuario)
    db.session.commit()
    return jsonify({'mensaje': 'Usuario eliminado'}), 200
