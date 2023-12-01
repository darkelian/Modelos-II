from database.database import db

class Estudiante(db.Model):
    __tablename__ = 'estudiante'
    carnet = db.Column(db.Integer, primary_key=True)
    nombre_completo = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    creado = db.Column(db.DateTime, server_default=db.func.current_timestamp())
    actualizado = db.Column(db.DateTime, server_default=db.func.current_timestamp())
