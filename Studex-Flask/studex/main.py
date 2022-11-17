from flask import redirect, render_template, request, Blueprint
from studex import create_app
from flask_login import login_required, logout_user, current_user
from studex.Services.LoginServices import logincheckout
from studex.DAO.FormDAO import form_add_user


app = Blueprint('app', __name__)
app = create_app()


@app.route('/')
def home():
    return render_template("home.html", user=current_user)


@app.route('/perfil')
@login_required
def perfil():
    return render_template("perfil.html", user=current_user)

@main.route('/pesquisar')
@login_required
def pesquisar():
    return render_template("pesquisar.html", user=current_user)


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        logincheckout(request.values.to_dict())

    return render_template("login.html", user=current_user)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/login')


@app.route("/forms", methods=["POST", "GET"])
def forms():
    if request.method == 'POST':

        form_add_user(list(request.values.values()))

    return render_template("forms.html", user=current_user)


if __name__ == '__main__':
    app.run(debug=True)
