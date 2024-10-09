from database import db
from datetime import datetime

class Inscripcion(db.Model):
    __tablename__ = 'inscripcion'

    id = db.Column(db.Integer, primary_key=True)
    fecha_inscripcion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # Clave foránea para el estudiante (usuario)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

    # Clave foránea para el curso
    curso_id = db.Column(db.Integer, db.ForeignKey('curso.id'), nullable=False)

    def __init__(self, usuario_id, curso_id):
        self.usuario_id = usuario_id
        self.curso_id = curso_id