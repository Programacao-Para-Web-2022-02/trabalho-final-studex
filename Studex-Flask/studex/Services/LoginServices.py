from flask import redirect, url_for, render_template, request, flash
from studex import create_app, db
from flask_login import login_user, login_required, logout_user, current_user
from studex.Models.Usuario import Usuario


def logincheckout(user: dict):

    usuario = Usuario.query.filter_by(email=user['email']).first()

    if not usuario:
        return flash('Usuário ou senha incorretos.', category='error')

    elif usuario.senha != user['password']:
        return flash('Usuário ou senha incorretos.', category='error')

    login_user(usuario)
    return flash('Login efetuado com sucesso', category='success')
