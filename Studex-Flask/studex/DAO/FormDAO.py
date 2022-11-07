from flask import redirect, url_for, render_template, request
# from studex.forms import Form, LoginForm
from studex import create_app, db
from studex.Models.Usuario import Usuario


def form_add_user(form, request_method):
    if request_method == 'POST':
        new_user = Usuario(usuario=form.username.data,
                        email=form.email.data,
                        senha=form.password.data,
                        nome=form.nome.data,
                        ra=form.ra.data,
                        tempo_prog=form.tempo_prog.data,
                        ling_pref=form.ling_pref.data,
                        sis_op=form.sis_op.data,
                        nivel_py=form.nivel_py.data,
                        nivel_js=form.nivel_js.data,
                        nivel_c=form.nivel_c.data,
                        nivel_htmlcss=form.nivel_htmlcss.data,
                        nivel_java=form.nivel_java.data,
                        resumo=form.resumo.data)

        db.session.add(new_user)
        db.session.commit()
        return f'<h1>Novo Usuário foi criado <br> Todos os Usuario = {User.query.all()}<br> !</h1> '