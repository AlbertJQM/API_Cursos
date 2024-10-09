from database import db

class Curso(db.Model):
    __tablename__ = 'curso'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(255), nullable=True)
    creditos = db.Column(db.Integer, nullable=False)

    # Relación con Lección (un curso tiene muchas lecciones)
    lecciones = db.relationship('Leccion', backref='curso', lazy=True)

    # Relación con Inscripción (un curso puede tener muchas inscripciones)
    inscripciones = db.relationship('Inscripcion', backref='curso', lazy=True)

    def __init__(self, nombre, descripcion, creditos):
        self.nombre = nombre
        self.descripcion = descripcion
        self.creditos = creditos