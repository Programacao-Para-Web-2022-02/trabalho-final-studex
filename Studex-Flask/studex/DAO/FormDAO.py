from flask import redirect, url_for, render_template, request, flash
# from studex.forms import Form, LoginForm
from __init__ import create_app, db
from Models.Usuario import Usuario


def form_add_user(form: list):

    email = form['em']
    user = Usuario.query.filter_by(email=email).first()

    if user:
        return flash('Usuário já cadastrado.', category='error')

    new_user = Usuario(
        usuario=form['nm'],
        email=form['em'],
        senha=form['pss'],
        ra=form['ra'],
        semestre=form['se'],
        tempo=form['tm'],
        linguagem=form['lg'],
        so=form['so'],
        python=form['py'],
        javascript=form['js'],
        c=form['c'],
        html=form['html'],
        java=form['jv'],
        resumo=form['rs'])

    db.session.add(new_user)
    db.session.commit()
    return flash('Usuário cadastrado com sucesso!', category='success')
