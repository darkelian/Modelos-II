from flask import Blueprint, request, jsonify
from database.database import db
from models.categoria import Categoria

categorias_bp = Blueprint('categorias_bp', __name__)

@categorias_bp.route('/', methods=['POST'])
def agregar_categoria():
    """
    Agrega una nueva categoría
    ---
    tags:
      - categorias
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        schema:
          id: Categoria
          required:
            - nombre
          properties:
            nombre:
              type: string
              description: El nombre de la categoría
    responses:
      201:
        description: Categoría agregada exitosamente
    """
    datos = request.get_json()
    nueva_categoria = Categoria(nombre=datos['nombre'])
    db.session.add(nueva_categoria)
    db.session.commit()
    return jsonify({'mensaje': 'Categoría agregada'}), 201

@categorias_bp.route('/', methods=['GET'])
def obtener_categorias():
    """
    Obtiene una lista de todas las categorías
    ---
    tags:
      - categorias
    responses:
      200:
        description: Lista de categorías
        schema:
          type: array
          items:
            $ref: '#/definitions/Categoria'
    definitions:
      Categoria:
        type: object
        properties:
          id:
            type: integer
          nombre:
            type: string
    """
    categorias = Categoria.query.all()
    return jsonify([{'id': cat.id, 'nombre': cat.nombre} for cat in categorias]), 200

@categorias_bp.route('/<int:id>', methods=['PUT'])
def actualizar_categoria(id):
    """
    Actualiza una categoría existente
    ---
    tags:
      - categorias
    consumes:
      - application/json
    parameters:
      - in: path
        name: id
        type: integer
        required: true
        description: ID de la categoría
      - in: body
        name: body
        schema:
          id: Categoria
          required:
            - nombre
          properties:
            nombre:
              type: string
              description: El nuevo nombre de la categoría
    responses:
      200:
        description: Categoría actualizada exitosamente
    """
    datos = request.get_json()
    categoria = Categoria.query.get_or_404(id)
    categoria.nombre = datos['nombre']
    db.session.commit()
    return jsonify({'mensaje': 'Categoría actualizada'}), 200

@categorias_bp.route('/<int:id>', methods=['DELETE'])
def eliminar_categoria(id):
    """
    Elimina una categoría
    ---
    tags:
      - categorias
    parameters:
      - in: path
        name: id
        type: integer
        required: true
        description: ID de la categoría
    responses:
      200:
        description: Categoría eliminada exitosamente
    """
    categoria = Categoria.query.get_or_404(id)
    db.session.delete(categoria)
    db.session.commit()
    return jsonify({'mensaje': 'Categoría eliminada'}), 200
