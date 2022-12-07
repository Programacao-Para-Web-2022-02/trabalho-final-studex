import MySQLdb.cursors
from flask import redirect, render_template, request, Blueprint, jsonify
from __init__ import create_app
from flask_login import login_required, logout_user, current_user
from Services.LoginServices import logincheck, salva_usuario
from DAO.FormDAO import form_add_user, db
from flask_googlemaps import GoogleMaps
from random import randint
from flask_mysqldb import MySQL, MySQLdb
from util import bd

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
    ling = request.form['ling']
    so = request.form['so']
    maistempo = request.form['maistempo']
    frase_select = "SELECT * FROM usuario"
    frase_lin = "SELECT * FROM usuario WHERE so LIKE 'lin%'"
    frase_win = "SELECT * FROM usuario WHERE so LIKE 'win%'"
    frase_mac = "SELECT * FROM usuario WHERE so LIKE 'mac%'"

    if ling == "nenhum":
        pass
    if so == "nenhum":
        pass
    if maistempo == "nenhum":
        pass
    if ling == "nenhum" and so == "nenhum" and maistempo == "nenhum":
        return f'<h1>Nenhum Filtro Selecionado!</h1>'

    if ling == "nenhum" and so == "Usuários de Linux" and maistempo == "nenhum":
        query = f"{frase_lin};"
    if ling == "nenhum" and so == "Usuários de Linux" and maistempo == "Semestre":
        query = f"{frase_lin} ORDER BY semestre DESC;"
    if ling == "nenhum" and so == "Usuários de Linux" and maistempo == "Maior tempo de programação":
        query = f"{frase_lin} ORDER BY tempo DESC;"

    if ling == "nenhum" and so == "Usuários de MacOS" and maistempo == "nenhum":
        query = f"{frase_mac}"
    if ling == "nenhum" and so == "Usuários de MacOS" and maistempo == "Semestre":
        query = f"{frase_mac} ORDER BY semestre DESC;"
    if ling == "nenhum" and so == "Usuários de MacOS" and maistempo == "Maior tempo de programação":
        query = f"{frase_mac} ORDER BY tempo DESC;"

    if ling == "nenhum" and so == "Usuários de Windows" and maistempo == "nenhum":
        query = f"{frase_win}"
    if ling == "nenhum" and so == "Usuários de Windows" and maistempo == "Semestre":
        query = f"{frase_win} ORDER BY semestre DESC;"
    if ling == "nenhum" and so == "Usuários de Windows" and maistempo == "Maior tempo de programação":
        query = f"{frase_win} ORDER BY tempo DESC;"

    if ling == "nenhum" and so == "nenhum" and maistempo == "Semestre":
        query = f"{frase_select} ORDER BY semestre DESC;"
    if ling == "nenhum" and so == "nenhum" and maistempo == "Maior tempo de programação":
        query = f"{frase_select} ORDER BY tempo DESC;"

    # Python
    if ling == "Melhores em Python":
        query = f"{frase_select} ORDER BY python DESC;"
    if ling == "Melhores em Python" and so == "Usuários de Linux" and maistempo == "nenhum":
        query = f"{frase_lin} and linguagem = 'python' ORDER BY python DESC;"
    if ling == "Melhores em Python" and so == "Usuários de Windows" and maistempo == "nenhum":
        query = f"{frase_win}' and linguagem = 'python' ORDER BY python DESC;"
    if ling == "Melhores em Python" and so == "Usuários de MacOS" and maistempo == "nenhum":
        query = f"{frase_mac} and linguagem = 'python' ORDER BY python DESC;"
    if ling == "Melhores em Python" and so == "Usuários de Linux" and maistempo == "Maior tempo de programação":
        query = f"{frase_lin} and linguagem = 'python' ORDER BY tempo DESC;"
    elif ling == "Melhores em Python" and so == "Usuários de Linux" and maistempo == "Semestre":
        query = f"{frase_lin} and linguagem = 'python' ORDER BY semestre DESC;"
    if ling == "Melhores em Python" and so == "Usuários de Windows" and maistempo == "Maior tempo de programação":
        query = f"{frase_win} and linguagem = 'python' ORDER BY tempo DESC;"
    elif ling == "Melhores em Python" and so == "Usuários de Windows" and maistempo == "Semestre":
        query = f"{frase_win} and linguagem = 'python' ORDER BY python semestre DESC;"
    if ling == "Melhores em Python" and so == "Usuários de MacOS" and maistempo == "Maior tempo de programação":
        query = f"{frase_mac}'mac%' and linguagem = 'python' ORDER BY tempo DESC;"
    elif ling == "Melhores em Python" and so == "Usuários de MacOS" and maistempo == "Semestre":
        query = f"{frase_mac} and linguagem = 'python' ORDER BY semestre DESC;"
    # JavaScript
    if ling == "Melhores em JavaScript":
        query = f"{frase_select} ORDER BY javascript DESC;"
    if ling == "Melhores em JavaScript" and so == "Usuários de Linux" and maistempo == "nenhum":
        query = f"{frase_lin} and linguagem = 'javascript' ORDER BY javascript DESC;"
    if ling == "Melhores em JavaScript" and so == "Usuários de Windows" and maistempo == "nenhum":
        query = f"{frase_win} and linguagem = 'javascript' ORDER BY javascript DESC;"
    if ling == "Melhores em JavaScript" and so == "Usuários de MacOS" and maistempo == "nenhum":
        query = f"{frase_mac} and linguagem = 'javascript' ORDER BY javascript DESC;"
    if ling == "Melhores em JavaScript" and so == "Usuários de Linux" and maistempo == "Maior tempo de programação":
        query = f"{frase_lin} and linguagem = 'javascript' ORDER BY tempo DESC;"
    elif ling == "Melhores em JavaScript" and so == "Usuários de Linux" and maistempo == "Semestre":
        query = f"{frase_lin} and linguagem = 'javascript' ORDER BY semestre DESC;"
    if ling == "Melhores em JavaScript" and so == "Usuários de Windows" and maistempo == "Maior tempo de programação":
        query = f"{frase_win} and linguagem = 'javascript' ORDER BY tempo DESC;"
    elif ling == "Melhores em JavaScript" and so == "Usuários de Windows" and maistempo == "Semestre":
        query = f"{frase_win} and linguagem = 'javascript' ORDER BY semestre DESC;"
    if ling == "Melhores em JavaScript" and so == "Usuários de MacOS" and maistempo == "Maior tempo de programação":
        query = f"{frase_mac} and linguagem = 'javascript' ORDER BY tempo DESC;"
    elif ling == "Melhores em JavaScript" and so == "Usuários de MacOS" and maistempo == "Semestre":
        query = f"{frase_mac} and linguagem = 'javascript' ORDER BY semestre DESC;"
    # C++
    if ling == "Melhores em C++":
        query = f"{frase_select} ORDER BY c DESC;"
    if ling == "Melhores em C++" and so == "Usuários de Linux" and maistempo == "nenhum":
        query = f"{frase_lin} and linguagem LIKE 'c%' ORDER BY c DESC;"
    if ling == "Melhores em C++" and so == "Usuários de Windows" and maistempo == "nenhum":
        query = f"{frase_win} and linguagem LIKE 'c%' ORDER BY c DESC;"
    if ling == "Melhores em C++" and so == "Usuários de MacOS" and maistempo == "nenhum":
        query = f"{frase_mac} and linguagem LIKE 'c%' ORDER BY c DESC;"

    if ling == "Melhores em C++" and so == "Usuários de Linux" and maistempo == "Maior tempo de programação":
        query = f"{frase_lin} and linguagem LIKE 'c%' ORDER BY tempo DESC;"
    elif ling == "Melhores em C++" and so == "Usuários de Linux" and maistempo == "Semestre":
        query = f"{frase_lin} and linguagem LIKE 'c%' ORDER BY semestre DESC;"
    if ling == "Melhores em C++" and so == "Usuários de Windows" and maistempo == "Maior tempo de programação":
        query = f"{frase_win} and linguagem LIKE 'c%' ORDER BY tempo DESC;"
    elif ling == "Melhores em C++" and so == "Usuários de Windows" and maistempo == "Semestre":
        query = f"{frase_win} and linguagem LIKE 'c%' ORDER BY semestre DESC;"
    if ling == "Melhores em C++" and so == "Usuários de MacOS" and maistempo == "Maior tempo de programação":
        query = f"{frase_mac} and linguagem LIKE 'c%' ORDER BY tempo DESC;"
    elif ling == "Melhores em C++" and so == "Usuários de MacOS" and maistempo == "Semestre":
        query = f"{frase_mac} and linguagem LIKE 'c%' ORDER BY semestre DESC;"
    # HTMLCSS
    if ling == "Melhores em htmlcss":
        query = f"{frase_select} ORDER BY html DESC;"
    if ling == "Melhores em htmlcss" and so == "Usuários de Linux" and maistempo == "nenhum":
        query = f"{frase_lin} and linguagem LIKE 'htm%' ORDER BY html DESC;"
    if ling == "Melhores em htmlcss" and so == "Usuários de Windows" and maistempo == "nenhum":
        query = f"{frase_win} and linguagem LIKE 'htm%' ORDER BY html DESC;"
    if ling == "Melhores em htmlcss" and so == "Usuários de MacOS" and maistempo == "nenhum":
        query = f"{frase_mac} and linguagem LIKE 'htm%' ORDER BY html DESC;"
    if ling == "Melhores em htmlcss" and so == "Usuários de Linux" and maistempo == "Maior tempo de programação":
        query = f"{frase_lin} and linguagem LIKE 'htm%' ORDER BY tempo DESC;"
    elif ling == "Melhores em htmlcss" and so == "Usuários de Linux" and maistempo == "Semestre":
        query = f"{frase_lin} and linguagem LIKE 'htm%' ORDER BY semestre DESC;"
    if ling == "Melhores em htmlcss" and so == "Usuários de Windows" and maistempo == "Maior tempo de programação":
        query = f"{frase_win} and linguagem = LIKE 'htm%' ORDER BY tempo DESC;"
    elif ling == "Melhores em htmlcss" and so == "Usuários de Windows" and maistempo == "Semestre":
        query = f"{frase_win} and linguagem LIKE 'htm%' ORDER BY semestre DESC;"
    if ling == "Melhores em htmlcss" and so == "Usuários de MacOS" and maistempo == "Maior tempo de programação":
        query = f"{frase_mac} and linguagem LIKE 'htm%' ORDER BY tempo DESC;"
    elif ling == "Melhores em htmlcss" and so == "Usuários de MacOS" and maistempo == "Semestre":
        query = f"{frase_mac} and linguagem LIKE 'htm%' ORDER BY semestre DESC;"
    # Java
    if ling == "Melhores em Java":
        query = f"{frase_select} ORDER BY java DESC;"
    if ling == "Melhores em Java" and so == "Usuários de Linux" and maistempo == "nenhum":
        query = f"{frase_lin} and linguagem = 'java' ORDER BY java DESC;"
    if ling == "Melhores em Java" and so == "Usuários de Windows" and maistempo == "nenhum":
        query = f"{frase_win} and linguagem = 'java' ORDER BY java DESC;"
    if ling == "Melhores em Java" and so == "Usuários de MacOS" and maistempo == "nenhum":
        query = f"{frase_mac} and linguagem = 'java' ORDER BY java DESC;"
    if ling == "Melhores em Java" and so == "Usuários de Linux" and maistempo == "Maior tempo de programação":
        query = f"{frase_lin} and linguagem = 'java' ORDER BY tempo DESC;"
    elif ling == "Melhores em Java" and so == "Usuários de Linux" and maistempo == "Semestre":
        query = f"{frase_lin} and linguagem = 'java' ORDER BY semestre DESC;"
    if ling == "Melhores em Java" and so == "Usuários de Windows" and maistempo == "Maior tempo de programação":
        query = f"{frase_win} and linguagem = 'java' ORDER BY tempo DESC;"
    elif ling == "Melhores em Java" and so == "Usuários de Windows" and maistempo == "Semestre":
        query = f"{frase_win} and linguagem = 'java' ORDER BY semestre DESC;"
    if ling == "Melhores em Java" and so == "Usuários de MacOS" and maistempo == "Maior tempo de programação":
        query = f"{frase_mac} and linguagem = 'java' ORDER BY tempo DESC;"
    elif ling == "Melhores em Java" and so == "Usuários de MacOS" and maistempo == "Semestre":
        query = f"{frase_mac} and linguagem = 'java' ORDER BY semestre DESC;"
    cur.execute(query)
    usuario = cur.fetchall()

    return render_template("filtros.html", user=current_user, usuario=usuario, n=randint(1, 10),
                           row=row, ling=ling, so=so, maistempo=maistempo)


@app.route('/perfil-singular', methods=["POST", "GET"])
@login_required
def perfil_singular():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        ra = request.form['ra-ind']
        query = f"SELECT * FROM usuario WHERE ra = '{ra}';"
        cur.execute(query)
        usuario = cur.fetchall()

    return render_template("perfil-singular.html", user=current_user, usuario=usuario, n=randint(1, 10), row=row)


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
    sql = bd.SQL('root', '123456', 'Studex')
    cmd = 'SELECT id, latitude, longitude FROM usuario;'
    cs = sql.consultar(cmd, [])
    marcadores = ''
    icone = "{icon:greenIcon}"
    for idt, lat, lng in cs:
        marcadores += 'var mk_{} = L.marker([{}, {}], {}).addTo(m);\n'.format(idt, lat, lng, icone)
        print(marcadores)
    cs.close()
    return render_template('mapa.html', marcadores=marcadores, user=current_user, usuario=usuario, n=randint(1, 10))



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
