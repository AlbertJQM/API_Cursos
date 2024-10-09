from flask import Blueprint, request, jsonify
from services.usuario_service import UsuarioService

usuarios_blueprint = Blueprint('usuarios', __name__)
usuario_service = UsuarioService()

@usuarios_blueprint.route('/login', methods=['POST'])
def login():
    data = request.json
    token = usuario_service.login(data['email'], data['contraseña'])
    if token:
        return jsonify({'token': token})
    return jsonify({'mensaje': 'Credenciales inválidas.'}), 401

@usuarios_blueprint.route('/', methods=['GET'])
def listar_usuarios():
    usuarios = usuario_service.listar_usuarios()
    return jsonify([{"id": usuario.id, "nombre": usuario.nombre, "paterno": usuario.paterno, "materno": usuario.materno, "ci": usuario.ci, "email": usuario.email, "rol": usuario.rol} for usuario in usuarios]), 200

@usuarios_blueprint.route('/<int:id>', methods=['GET'])
def mostrar_usuario(id):
    usuario = usuario_service.mostrar_usuario(id)
    if usuario:
        return jsonify({"id": usuario.id, "nombre": usuario.nombre, "paterno": usuario.paterno, "materno": usuario.materno, "ci": usuario.ci, "email": usuario.email, "rol": usuario.rol}), 200
    return jsonify({'mensaje': 'Usuario no encontrado.'}), 404

@usuarios_blueprint.route('/', methods=['POST'])
def crear_usuario():
    data = request.get_json()
    nombre = data.get('nombre')
    paterno = data.get('paterno')
    materno = data.get('materno')
    ci = data.get('ci')
    email = data.get('email')
    contraseña = data.get('contraseña')
    rol = data.get('rol')
    
    if not (nombre and paterno and materno and ci and email and contraseña and rol):
        print(data)
        return jsonify({"error": "Faltan datos."}), 400
    
    nuevo_usuario = usuario_service.crear_usuario(nombre, paterno, materno, ci, email, contraseña, rol)
    return jsonify({"mensaje": "Usuario registrado.", "usuario": {"id": nuevo_usuario.id, "nombre": nuevo_usuario.nombre, "paterno": nuevo_usuario.paterno, "materno": nuevo_usuario.materno, "ci": nuevo_usuario.ci, "email": nuevo_usuario.email, "rol": nuevo_usuario.rol}}), 201

@usuarios_blueprint.route('/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    data = request.get_json()
    nombre = data.get('nombre')
    paterno = data.get('paterno')
    materno = data.get('materno')
    ci = data.get('ci')
    email = data.get('email')
    contraseña = data.get('contraseña')
    rol = data.get('rol')
    
    usuario_actualizado = usuario_service.actualizar_usuario(id, nombre, paterno, materno, ci, email, contraseña, rol)
    if usuario_actualizado:
        return jsonify({"mensaje": "Usuario actualizado.", "usuario": {"id": usuario_actualizado.id, "nombre": usuario_actualizado.nombre, "paterno": usuario_actualizado.paterno, "materno": usuario_actualizado.materno, "ci": usuario_actualizado.ci, "email": usuario_actualizado.email, "rol": usuario_actualizado.rol}}), 200
    return jsonify({"error": "Usuario no encontrado."}), 404

@usuarios_blueprint.route('/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    usuario_eliminado = usuario_service.eliminar_usuario(id)
    if usuario_eliminado:
        return jsonify({"mensaje": "Usuario eliminado."}), 200
    return jsonify({"error": "Usuario no encontrado."}), 404