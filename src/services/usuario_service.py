from werkzeug.security import check_password_hash
from repositories.usuario_repository import UsuarioRepository
from utils.jwt import generar_token_jwt

class UsuarioService():
    def __init__(self) -> None:
        self.usuario_repository = UsuarioRepository()
    
    def login(self, email, contraseña):
        usuario = self.usuario_repository.get_usuario_email(email)
        if usuario and check_password_hash(usuario.contraseña, contraseña):
            return generar_token_jwt(usuario)
        return None
    def listar_usuarios(self):
        return self.usuario_repository.get_usuarios()
    
    def mostrar_usuario(self, id):
        return self.usuario_repository.get_usuario(id)
    
    def crear_usuario(self, nombre, paterno, materno, ci, email, contraseña, rol):
        return self.usuario_repository.post_usuario(nombre, paterno, materno, ci, email, contraseña, rol)    

    def actualizar_usuario(self, id, nombre, paterno, materno, ci, email, contraseña, rol):
        return self.usuario_repository.actualizar_usuario(id, nombre, paterno, materno, ci, email, contraseña, rol)

    def eliminar_usuario(self, id):
        return self.usuario_repository.eliminar_usuario(id)