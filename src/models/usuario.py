from database import db

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    paterno = db.Column(db.String(30), nullable=True)
    materno = db.Column(db.String(30), nullable=False)
    ci = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    contraseña = db.Column(db.String(255), nullable=False)
    rol = db.Column(db.Integer, nullable=False) #Instructor o Estudiante
    
    inscripciones = db.relationship('Inscripcion', backref='usuario', lazy=True)

    def __init__(self, nombre, paterno, materno, ci, email, contraseña, rol) -> None:
        self.nombre = nombre
        self.paterno = paterno
        self.materno = materno
        self.ci = ci
        self.email = email
        self.contraseña = contraseña
        self.rol = rol