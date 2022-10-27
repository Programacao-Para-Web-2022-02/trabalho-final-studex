from flask import Flask, redirect, url_for, render_template, request
from studex.forms import LoginForm, RegisterForm
from studex import app, db
from studex.models import users

@app.route('/')
def home():
    return render_template("home.html")

#Registro
@app.route("/registro", methods=["POST", "GET"])
def registro():
    form = RegisterForm()

    if form.validate_on_submit():
        new_user = users(usename=form.username.data, email=form.email.data, senha=form.password.data)
        db.session.add(new_user)
        db.session.commit()

        return f'<h1>Novo Usuário foi criado <br> Todos os Usuario = {users.usename, users.email}<br> !</h1> '

    return render_template("registro.html", form=form)

#Login
@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = users.query.filter_by(usename=form.username.data).first()
        if user:
            if user.senha == form.password.data:
                return redirect(url_for("form"))

        return '<h1> usuário ou senha inválida </h1>'
        #return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template("login.html", form=form)

@app.route("/logout")
def logout():
    return render_template("signup.html")

@app.route("/form", methods=["POST", "GET"])
def form():

    form = RegisterForm()

    if form.validate_on_submit():
        new_user = users(usuario=form.username.data, email=form.email.data, 
                        senha=form.password.data, nome=form.nome.data, ra=form.ra.data, 
                        tempo_prog=form.tempo_prog.data, ling_pref=form.ling_pref.data, 
                        sis_op=form.sis_op.data, nivel_py=form.nivel_py.data, 
                        nivel_c=form.nivel_c.data, nivel_htmlcss=form.nivel_htmlcss.data,
                        nivel_java=form.nivel_java.data, resumo=form.resumo.data)
        db.session.add(new_user)
        db.session.commit()
        
        return f'<h1>Novo Usuário foi criado <br> Todos os Usuario = {users.query.all()}<br> !</h1> '

    return render_template("form.html", form=form)
    