from flask import redirect, render_template, request, Blueprint
from __init__ import create_app
from flask_login import login_required, logout_user, current_user
from Services.LoginServices import logincheck, salva_usuario
from DAO.FormDAO import form_add_user
from Models.Usuario import Usuario


main = Blueprint('app', __name__)
app = create_app()


@app.route('/')
def home():

    return render_template("home.html", user=current_user)


@app.route('/perfil')
@login_required
def perfil():
    
    return render_template("perfil.html", user=current_user, usuario=salva_usuario(current_user.get_id()))


@app.route('/pesquisar')
@login_required
def pesquisar():
    return render_template("pesquisar.html", user=current_user)


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
