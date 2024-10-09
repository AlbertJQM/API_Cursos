from database import db

class Leccion(db.Model):
    __tablename__ = 'leccion'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    contenido = db.Column(db.Text, nullable=False)

    # Clave foránea para el curso
    curso_id = db.Column(db.Integer, db.ForeignKey('curso.id'), nullable=False)

    def __init__(self, titulo, contenido, curso_id):
        self.titulo = titulo
        self.contenido = contenido
        self.curso_id = curso_id