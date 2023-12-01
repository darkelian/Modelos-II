from database.database import db

class Usuario(db.Model):
    __tablename__ = 'usuario'
    email = db.Column(db.String(64), primary_key=True)
    clave = db.Column(db.String(255), nullable=False)
    rol_id = db.Column(db.Integer, db.ForeignKey('rol.id'), nullable=False)
    creado = db.Column(db.DateTime, server_default=db.func.current_timestamp())
    actualizado = db.Column(db.DateTime, server_default=db.func.current_timestamp())
