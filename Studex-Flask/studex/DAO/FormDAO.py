from flask import redirect, url_for, render_template, request, flash
# from studex.forms import Form, LoginForm
from studex import create_app, db
from studex.Models.Usuario import Usuario


def form_add_user(form: list):

    email = form[1]
    user = Usuario.query.filter_by(email=email).first()

    if user:
        return False

    new_user = Usuario(
        usuario=form[0],
        email=form[1],
        senha=form[2],
        ra=form[3],
        semestre=form[4],
        tempo=form[5],
        linguagem=form[6],
        so=form[7],
        python=form[8],
        javascript=form[9],
        c=form[10],
        html=form[11],
        java=form[12],
        resumo=form[13])

    db.session.add(new_user)
    db.session.commit()
    return True
