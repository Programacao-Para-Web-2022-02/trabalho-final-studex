from flask import redirect, url_for, render_template, request, Blueprint, flash, Response, jsonify
from studex import create_app, db
from flask_login import login_user, login_required, logout_user, current_user
from studex.Models.Usuario import Usuario
from studex.Services.LoginServices import logincheckout
from studex.DAO.FormDAO import form_add_user


main = Blueprint('main', __name__)
app = create_app()

@main.route('/')
def home():
    return render_template("home.html")

# Login
@main.route('/perfil')
def perfil():
    return render_template("perfil.html")

@main.route("/login", methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        print(list(request.values.values()))
        logincheckout(list(request.values.values()))

    return render_template("login.html")

@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/login')

@main.route("/forms", methods=["POST", "GET"])
def forms():
    if request.method == 'POST':

        form_add_user(list(request.values.values()))

    return render_template("forms.html")

if __name__ == '__main__':
    app.run(debug=True)
