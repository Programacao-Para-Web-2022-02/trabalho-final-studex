import MySQLdb.cursors
from flask import redirect, render_template, request, Blueprint, jsonify, url_for
from __init__ import create_app
from flask_login import login_required, logout_user, current_user
from Services.LoginServices import logincheck, salva_usuario
from DAO.FormDAO import form_add_user, db
from flask_googlemaps import GoogleMaps
# from flask_googlemaps import Map
from random import randint
from flask_mysqldb import MySQL, MySQLdb

# from Models import Usuario


main = Blueprint('app', __name__)
app = create_app()
GoogleMaps(app, key="8JZ7i18MjFuM35dJHq70n3Hx4")
usuario = ''
mysql = MySQL(app)
row = 0


@app.route('/')
def home():
    return render_template("home.html", user=current_user)


@app.route('/editar', methods=["POST", "GET"])
@login_required
def editar():
    global usuario
    if request.method == 'POST':
        print(request.values.to_dict())
        print(current_user.ra)
        current_user.usuario = request.form['nm']
        current_user.email = request.form['em']
        current_user.senha = request.form['pss']
        current_user.ra = request.form['ra']
        current_user.semestre = request.form['se']
        current_user.tempo = request.form['tm']
        current_user.linguagem = request.form['lg']
        current_user.so = request.form['so']
        current_user.python = request.form['py']
        current_user.javascript = request.form['js']
        current_user.c = request.form['c']
        current_user.html = request.form['html']
        current_user.java = request.form['jv']
        current_user.resumo = request.form['rs']
        db.session.commit()

    return render_template("editar.html", user=current_user, usuario=salva_usuario(current_user.get_id()))


@app.route('/filtros', methods=["POST", "GET"])
@login_required
def filtros():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        ling = request.form['ling']
        so = request.form['so']
        maistempo = request.form['maistempo']

        # Python
        if ling == "Melhores em Python" and so == "Usuários de Linux" and maistempo == "Maior tempo de programação":
            query = "SELECT * FROM usuario WHERE so LIKE 'lin%' and linguagem = 'python' ORDER BY python DESC, tempo DESC;"
        elif ling == "Melhores em Python" and so == "Usuários de Linux" and maistempo == "Semestre":
            query = "SELECT * FROM usuario WHERE so LIKE 'lin%' and linguagem = 'python' ORDER BY python DESC, semestre DESC;"
        if ling == "Melhores em Python" and so == "Usuários de Windows" and maistempo == "Maior tempo de programação":
            query = "SELECT * FROM usuario WHERE so LIKE 'win%' and linguagem = 'python' ORDER BY python DESC, tempo DESC;"
        elif ling == "Melhores em Python" and so == "Usuários de Windows" and maistempo == "Semestre":
            query = "SELECT * FROM usuario WHERE so LIKE 'win%' and linguagem = 'python' ORDER BY python DESC, semestre DESC;"
        if ling == "Melhores em Python" and so == "Usuários de MacOS" and maistempo == "Maior tempo de programação":
            query = "SELECT * FROM usuario WHERE so LIKE 'mac%' and linguagem = 'python' ORDER BY python DESC, tempo DESC;"
        elif ling == "Melhores em Python" and so == "Usuários de MacOS" and maistempo == "Semestre":
            query = "SELECT * FROM usuario WHERE so LIKE 'mac%' and linguagem = 'python' ORDER BY python DESC, semestre DESC;"

        # JavaScript
        if ling == "Melhores em JavaScript" and so == "Usuários de Linux" and maistempo == "Maior tempo de programação":
            query = "SELECT * FROM usuario WHERE so LIKE 'lin%' and linguagem = 'javascript' ORDER BY javascript DESC, tempo DESC;"
        elif ling == "Melhores em JavaScript" and so == "Usuários de Linux" and maistempo == "Semestre":
            query = "SELECT * FROM usuario WHERE so LIKE 'lin%' and linguagem = 'javascript' ORDER BY javascript DESC, semestre DESC;"
        if ling == "Melhores em JavaScript" and so == "Usuários de Windows" and maistempo == "Maior tempo de programação":
            query = "SELECT * FROM usuario WHERE so LIKE 'win%' and linguagem = 'javascript' ORDER BY javascript DESC, tempo DESC;"
        elif ling == "Melhores em JavaScript" and so == "Usuários de Windows" and maistempo == "Semestre":
            query = "SELECT * FROM usuario WHERE so LIKE 'win%' and linguagem = 'javascript' ORDER BY javascript DESC, semestre DESC;"
        if ling == "Melhores em JavaScript" and so == "Usuários de MacOS" and maistempo == "Maior tempo de programação":
            query = "SELECT * FROM usuario WHERE so LIKE 'mac%' and linguagem = 'javascript' ORDER BY javascript DESC, tempo DESC;"
        elif ling == "Melhores em JavaScript" and so == "Usuários de MacOS" and maistempo == "Semestre":
            query = "SELECT * FROM usuario WHERE so LIKE 'mac%' and linguagem = 'javascript' ORDER BY javascript DESC, semestre DESC;"

        # C++
        if ling == "Melhores em C++" and so == "Usuários de Linux" and maistempo == "Maior tempo de programação":
            query = f"SELECT * FROM usuario WHERE so LIKE 'lin%' and linguagem = 'c' ORDER BY c DESC, tempo DESC;"
        elif ling == "Melhores em C++" and so == "Usuários de Linux" and maistempo == "Semestre":
            query = f"SELECT * FROM usuario WHERE so LIKE 'lin%' and linguagem = 'c' ORDER BY c DESC, semestre DESC;"
        if ling == "Melhores em C++" and so == "Usuários de Windows" and maistempo == "Maior tempo de programação":
            query = f"SELECT * FROM usuario WHERE so LIKE 'win%' and linguagem = 'c' ORDER BY c DESC, tempo DESC;"
        elif ling == "Melhores em C++" and so == "Usuários de Windows" and maistempo == "Semestre":
            query = f"SELECT * FROM usuario WHERE so LIKE 'win%' and linguagem = 'c' ORDER BY c DESC, semestre DESC;"
        if ling == "Melhores em C++" and so == "Usuários de MacOS" and maistempo == "Maior tempo de programação":
            query = f"SELECT * FROM usuario WHERE so LIKE 'mac%' and linguagem = 'c' ORDER BY c DESC, tempo DESC;"
        elif ling == "Melhores em C++" and so == "Usuários de MacOS" and maistempo == "Semestre":
            query = f"SELECT * FROM usuario WHERE so LIKE 'mac%' and linguagem = 'c' ORDER BY c DESC, semestre DESC;"

        # HTMLCSS
        if ling == "Melhores em htmlcss" and so == "Usuários de Linux" and maistempo == "Maior tempo de programação":
            query = "SELECT * FROM usuario WHERE so LIKE 'lin%' and linguagem = 'html' ORDER BY htmlcss DESC, tempo DESC;"
        elif ling == "Melhores em htmlcss" and so == "Usuários de Linux" and maistempo == "Semestre":
            query = "SELECT * FROM usuario WHERE so LIKE 'lin%' and linguagem = 'html' ORDER BY htmlcss DESC, semestre DESC;"
        if ling == "Melhores em htmlcss" and so == "Usuários de Windows" and maistempo == "Maior tempo de programação":
            query = "SELECT * FROM usuario WHERE so LIKE 'win%' and linguagem = 'html' ORDER BY htmlcss DESC, tempo DESC;"
        elif ling == "Melhores em htmlcss" and so == "Usuários de Windows" and maistempo == "Semestre":
            query = "SELECT * FROM usuario WHERE so LIKE 'win%' and linguagem = 'html' ORDER BY htmlcss DESC, semestre DESC;"
        if ling == "Melhores em htmlcss" and so == "Usuários de MacOS" and maistempo == "Maior tempo de programação":
            query = "SELECT * FROM usuario WHERE so LIKE 'mac%' and linguagem = 'html' ORDER BY html DESC, tempo DESC;"
        elif ling == "Melhores em htmlcss" and so == "Usuários de MacOS" and maistempo == "Semestre":
            query = "SELECT * FROM usuario WHERE so LIKE 'mac%' and linguagem = 'html' ORDER BY html DESC, semestre DESC;"

        # Java
        if ling == "Melhores em Java" and so == "Usuários de Linux" and maistempo == "Maior tempo de programação":
            query = "SELECT * FROM usuario WHERE so LIKE 'lin%' and linguagem = 'java' ORDER BY java DESC, tempo DESC;"
        elif ling == "Melhores em Java" and so == "Usuários de Linux" and maistempo == "Semestre":
            query = "SELECT * FROM usuario WHERE so LIKE 'lin%' and linguagem = 'java' ORDER BY java DESC, semestre DESC;"
        if ling == "Melhores em Java" and so == "Usuários de Windows" and maistempo == "Maior tempo de programação":
            query = "SELECT * FROM usuario WHERE so LIKE 'win%' and linguagem = 'java' ORDER BY java DESC, tempo DESC;"
        elif ling == "Melhores em Java" and so == "Usuários de Windows" and maistempo == "Semestre":
            query = "SELECT * FROM usuario WHERE so LIKE 'win%' and linguagem = 'java' ORDER BY java DESC, semestre DESC;"
        if ling == "Melhores em Java" and so == "Usuários de MacOS" and maistempo == "Maior tempo de programação":
            query = "SELECT * FROM usuario WHERE so LIKE 'mac%' and linguagem = 'java' ORDER BY java DESC, tempo DESC;"
        elif ling == "Melhores em Java" and so == "Usuários de MacOS" and maistempo == "Semestre":
            query = "SELECT * FROM usuario WHERE so LIKE 'mac%' and linguagem = 'java' ORDER BY java DESC, semestre DESC;"

        cur.execute(query)
        usuario = cur.fetchall()

        return render_template("filtros.html", user=current_user, usuario=usuario, n=randint(1, 10), row=row,
                               ling=ling, so=so, maistempo=maistempo)


@app.route('/perfil-singular', methods=["POST", "GET"])
@login_required
def perfil_singular():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        ra = request.form['ra-ind']
        query = f"SELECT * FROM usuario WHERE ra = '{ra}';"
        cur.execute(query)
        usuario = cur.fetchall()

    return render_template("perfil-singular.html", user=current_user, usuario=usuario,
                           n=randint(1, 10), row=row)


@app.route('/perfil')
@login_required
def perfil():
    return render_template("perfil.html", user=current_user, usuario=salva_usuario(current_user.get_id()),
                           n=randint(1, 10))


@app.route('/pesquisar')
@login_required
def pesquisar():
    return render_template("pesquisar.html", user=current_user)


@app.route("/ajaxlivesearch", methods=["POST", "GET"])
def ajaxlivesearch():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        search_word = request.form['query']
        print(search_word)
        if search_word == " ":
            query = "SELECT * from usuario"
            cur.execute(query)
            usuario = cur.fetchall()
        elif search_word != " ":
            query = f"SELECT * FROM usuario WHERE usuario LIKE '{search_word}%';"
            cur.execute(query)
            usuario = cur.fetchall()

    return jsonify({'htmlresponse': render_template('response.html', usuario=usuario, row=row)})


@app.route("/mapa")
def mapview():
    return render_template('mapa.html', user=current_user)


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        logincheck(request.values.to_dict())

    return render_template("login.html", user=current_user)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/login')


@app.route("/forms", methods=["POST", "GET"])
def forms():
    if request.method == 'POST':
        print(request.values.to_dict())
        form_add_user(request.values.to_dict())

    return render_template("forms.html", user=current_user)


if __name__ == '__main__':
    app.run(debug=True)
