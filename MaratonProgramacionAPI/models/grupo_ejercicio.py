from database.database import db

class GrupoEjercicio(db.Model):
    __tablename__ = 'grupo_ejercicio'
    grupo_id = db.Column(db.Integer, db.ForeignKey('grupo.id'), primary_key=True)
    ejercicio_id = db.Column(db.Integer, db.ForeignKey('ejercicio.id'), primary_key=True)
    solucion = db.Column(db.String(4096))
    duracion_solucion = db.Column(db.Integer)
    maraton_id = db.Column(db.Integer, db.ForeignKey('maraton.id'), nullable=False)
    creado = db.Column(db.DateTime, server_default=db.func.current_timestamp())
    actualizado = db.Column(db.DateTime, server_default=db.func.current_timestamp())
