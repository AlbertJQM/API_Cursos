class UsuarioDTO():
    def __init__(self, id, nombre, paterno, materno, ci, email, contraseña, rol) -> None:
        self.id = id
        self.nombre = nombre
        self.paterno = paterno
        self.materno = materno
        self.ci = ci
        self.email = email
        self.contraseña = contraseña
        self.rol = rol