from models.usuario import Usuario
from database import db

class UsuarioDAO():
    def get_usuario_por_id(self, id):
        return Usuario.query.get(id)
    
    def get_usuario_por_email(self, email):
        return Usuario.query.filter_by(emaild=email).first()
    
    def get_usuarios(self):
        return Usuario.query.all()
    
    def post_usuario(self, usuario):
        db.session.add(usuario)
        db.session.commit()
        return usuario
        
    def put_usuario(self, usuario):
        db.session.commit()
        return usuario
    
    def delete_usuario(self, usuario):
        db.session.delete(usuario)
        db.session.commit()
        return usuario
