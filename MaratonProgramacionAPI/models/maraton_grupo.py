from database.database import db

class MaratonGrupo(db.Model):
    __tablename__ = 'maraton_grupo'
    maraton_id = db.Column(db.Integer, db.ForeignKey('maraton.id'), primary_key=True)
    grupo_id = db.Column(db.Integer, db.ForeignKey('grupo.id'), primary_key=True)
    creado = db.Column(db.DateTime, server_default=db.func.current_timestamp())
    actualizado = db.Column(db.DateTime, server_default=db.func.current_timestamp())
