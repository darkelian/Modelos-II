from database.database import db

class Ejercicio(db.Model):
    __tablename__ = 'ejercicio'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    enunciado = db.Column(db.String(2048), nullable=False)
    creado = db.Column(db.DateTime, server_default=db.func.current_timestamp())
    actualizado = db.Column(db.DateTime, server_default=db.func.current_timestamp())
