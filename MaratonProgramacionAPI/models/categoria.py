from database.database import db

class Categoria(db.Model):
    __tablename__ = 'categoria'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(32), nullable=False)
    creado = db.Column(db.DateTime, server_default=db.func.current_timestamp())
    actualizado = db.Column(db.DateTime, server_default=db.func.current_timestamp())
