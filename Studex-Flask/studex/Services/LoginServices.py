from flask import redirect, url_for, render_template, request, flash
from __init__ import create_app, db
from flask_login import login_user, login_required, logout_user, current_user
from Models.Usuario import Usuario

usuario = None



def logincheck(user: dict):

    global usuario
    usuario = Usuario.query.filter_by(email=user['email']).first()

    if not usuario:
        return flash('Usuário ou senha incorretos.', category='error')

    elif usuario.senha != user['password']:
        return flash('Usuário ou senha incorretos.', category='error')

    login_user(usuario, remember=True)
    return flash('Login efetuado com sucesso', category='success')


def salva_usuario(id):
    usuario = Usuario.query.filter_by(id=id).first()

    return usuario
