import jwt
from flask import request, jsonify
from functools import wraps
from config import Config
#from services.usuario_service import UsuarioService

def token_requerido(f):
    @wraps(f)
    def decorador(*args, **kwargs):
        token = request.headers.get('x-access-token')
        if not token:
            return jsonify({'mensaje': 'Token faltante.'}), 401
        try:
            datos = jwt.decode(token, Config.SECRET_KEY, algorithms=['HS256'])
            current_user = UsuarioService.mostrar_usuario(datos['id'])
        except:
            return jsonify({'mensaje': 'Token inválido.'}), 401
        return f(current_user, *args, **kwargs)
    return decorador

def generar_token_jwt(usuario):
    token = jwt.encode({'id': usuario.id, 'rol': usuario.rol}, Config.SECRET_KEY, algorithm='HS256')
    return token