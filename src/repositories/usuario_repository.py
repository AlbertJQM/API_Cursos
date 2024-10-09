from werkzeug.security import generate_password_hash
from dao.usuario_dao import UsuarioDAO
from dto.usuario_dto import UsuarioDTO
from models.usuario import Usuario

class UsuarioRepository():
    def __init__(self) -> None:
        self.usuario_dao = UsuarioDAO()
    
    def get_usuario(self, id):
        usuario = self.usuario_dao.get_usuario_por_id(id)
        if usuario:
            usuario_dto = UsuarioDTO(usuario.id, usuario.nombre, usuario.paterno, usuario.materno, usuario.ci, usuario.email, usuario.contraseña, usuario.rol)
            return usuario_dto
        return None            

    def get_usuario_email(self, email):
        usuario = self.usuario_dao.get_usuario_por_email(email)
        if usuario:
            usuario_dto = UsuarioDTO(usuario.id, usuario.nombre, usuario.paterno, usuario.materno, usuario.ci, usuario.email, usuario.contraseña, usuario.rol)
            return usuario_dto
        return None

    def get_usuarios(self):
        usuarios = self.usuario_dao.get_usuarios()
        if usuarios:
            usuarios_dto = []
            for usuario in usuarios:
                usuario_dto = UsuarioDTO(usuario.id, usuario.nombre, usuario.paterno, usuario.materno, usuario.ci, usuario.email, usuario.contraseña, usuario.rol)
                usuarios_dto.append(usuario_dto)
            return usuarios_dto
        return None

    def post_usuario(self, nombre, paterno, materno, ci, email, contraseña, rol):
        hashed_password = generate_password_hash(contraseña)
        nuevo_usuario = Usuario(nombre=nombre, paterno=paterno, materno=materno, ci=ci, email=email, contraseña=hashed_password, rol=rol)
        return self.usuario_dao.post_usuario(nuevo_usuario)

    def actualizar_usuario(self, id, nombre, paterno, materno, ci, email, contraseña, rol):
        usuario = self.usuario_dao.get_usuario_por_id(id)
        if usuario:
            usuario.nombre = nombre
            usuario.paterno = paterno
            usuario.materno = materno
            usuario.ci = ci
            usuario.email = email
            usuario.rol = rol
            if contraseña:
                usuario.contraseña = generate_password_hash(contraseña)
            return self.usuario_dao.put_usuario(usuario)
        return None

    def eliminar_usuario(self, id):
        usuario = self.usuario_dao.get_usuario_por_id(id)
        if usuario:
            return self.usuario_dao.delete_usuario(usuario)
        return None