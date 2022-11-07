from flask import redirect, url_for, render_template, request
# from studex.forms import Form, LoginForm
from studex import create_app, db
from studex.Models.Usuario import Usuario


def logincheckout(form):
    form = LoginForm()
    if form.validate_on_submit():
        user = Usuario.query.filter_by(usename=form.username.data).first()
        if user:
            if user.senha == form.password.data:
                return redirect(url_for("home"))

        return '<h1> usuário ou senha inválida </h1>'
