from database.database import db

class EstudianteCurso(db.Model):
    __tablename__ = 'estudiante_curso'
    estudiante_carnet = db.Column(db.Integer, db.ForeignKey('estudiante.carnet'), primary_key=True)
    curso_id = db.Column(db.Integer, db.ForeignKey('curso.id'), primary_key=True)
    creado = db.Column(db.DateTime, server_default=db.func.current_timestamp())
    actualizado = db.Column(db.DateTime, server_default=db.func.current_timestamp())
