from flask import flash
from flask_login import login_user
from Models.Usuario import Usuario
from werkzeug.security import check_password_hash


def logincheck(user: dict):

    usuario = Usuario.query.filter_by(email=user['email']).first()

    if not usuario:
        return flash('Usuário ou senha incorretos.', category='error')

    elif check_password_hash(usuario.senha, user['password']):
        return flash('Usuário ou senha incorretos.', category='error')

    login_user(usuario, remember=True)
    return flash('Login efetuado com sucesso', category='success')


def salva_usuario(id):
    usuario = Usuario.query.filter_by(id=id).first()

    return usuario
