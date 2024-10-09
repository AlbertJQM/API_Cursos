from flask import Flask
from database import db
from routes.usuarios import usuarios_blueprint

app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)

#Registro de Blueprints
app.register_blueprint(usuarios_blueprint, url_prefix='/api/usuarios')

# Importar modelos aquí para que SQLAlchemy pueda encontrarlos
from models.usuario import Usuario
from models.curso import Curso
from models.leccion import Leccion
from models.inscripcion import Inscripcion

# Crear las tablas en la base de datos
with app.app_context():
    db.create_all()  # Crea las tablas

if __name__ == '__main__':
    app.run(debug=True)