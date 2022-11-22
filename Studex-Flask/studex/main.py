from flask import redirect, render_template, request, Blueprint
from __init__ import create_app
from flask_login import login_required, logout_user, current_user
from studex.Services.LoginServices import logincheckout, salva_usuario
from studex.DAO.FormDAO import form_add_user
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from random import randint


main = Blueprint('app', __name__)
app = create_app()
GoogleMaps(app, key="8JZ7i18MjFuM35dJHq70n3Hx4")
usuario = ''

n = randint(1, 10)
imagem = "static/assets/images/poke" + str(n) + ".png"

@app.route('/')
def home():

    return render_template("home.html", user=current_user)

@app.route('/editar')
@login_required
def editar():
    global usuario
    return render_template("editar.html", user=current_user, usuario=usuario)

@app.route('/perfil')
@login_required
def perfil():
    
    return render_template("perfil.html", user=current_user, usuario=salva_usuario(current_user.get_id()))

@app.route('/pesquisar')
@login_required
def pesquisar():
    return render_template("pesquisar.html", user=current_user)

@app.route("/mapa")
def mapview():
    mymap = Map(
        identifier="view-side",
        lat=37.4419,
        lng=-122.1419,
        markers=[(37.4419, -122.1419)]
    )
    sndmap = Map(
        identifier="sndmap",
        lat=37.4419,
        lng=-122.1419,
        markers=[
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
             'lat': 37.4419,
             'lng': -122.1419,
             'infobox': "<b>Hello World</b>"
          },
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
             'lat': 37.4300,
             'lng': -122.1400,
             'infobox': "<b>Hello World from other place</b>"
          }
        ]
    )
    return render_template('mapa.html', mymap=mymap, sndmap=sndmap, user=current_user)

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