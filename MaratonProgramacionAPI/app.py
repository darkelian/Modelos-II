from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_swagger import swagger

from routes.categorias_routes import categorias_bp
from routes.curso_routes import cursos_bp
from routes.ejercicio_routes import ejercicios_bp
from routes.estudiante_curso_routes import estudiante_curso_bp
from routes.estudiante_routes import estudiantes_bp
from routes.grupo_ejercicio_routes import grupo_ejercicio_bp
from routes.grupo_routes import grupo_bp
from routes.maraton_routes import maraton_bp
from routes.rol_routes import rol_bp
from routes.usuario_routes import usuario_bp

from database.database import db

app = Flask(__name__)

app.register_blueprint(categorias_bp, url_prefix='/categoria')
app.register_blueprint(estudiantes_bp, url_prefix='/estudiante')
app.register_blueprint(cursos_bp, url_prefix='/curso')
app.register_blueprint(ejercicios_bp, url_prefix='/ejercicio')
app.register_blueprint(estudiante_curso_bp, url_prefix='/estudiante_curso')
app.register_blueprint(grupo_ejercicio_bp, url_prefix='/grupo_ejercicio')
app.register_blueprint(grupo_bp, url_prefix='/grupo')
app.register_blueprint(maraton_bp, url_prefix='/maraton')
app.register_blueprint(rol_bp, url_prefix='/rol')
app.register_blueprint(usuario_bp, url_prefix='/usuario')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost/maraton'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
db.init_app(app)

@app.route('/swagger')
def spec():
    """
    prueba
    """
    return jsonify(swagger(app))
if __name__ == '__main__':
    app.run(debug=True, port=8081)
