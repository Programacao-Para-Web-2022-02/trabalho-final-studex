from flask import redirect, url_for, render_template, request, Blueprint, flash, Response, jsonify
# from studex.forms import Form, LoginForm
from __init__ import create_app
from studex.Services.LoginServices import logincheckout
from studex.DAO.FormDAO import form_add_user

# main = Blueprint('main', __name__)
app = create_app()


@app.route('/')
def home():
    print()
    return render_template("forms.html")

# Login


@app.route("/login", methods=["POST", "GET"])
def login():
    # form = LoginForm()
    logincheckout(form)

    return render_template("login.html")


@app.route("/form", methods=["POST", "GET"])
def form():
    # form = Form()
    # form_add_user(form)
    return render_template("form.html")


@app.route("/forms", methods=['GET', "POST"])
def forms():
    if request.method == 'POST':

        if not form_add_user(list(request.values.values())):
            flash('Usuário já existe.', category='error')

        else:
            flash('Usuário cadastrado com sucesso!', category='success')

    return render_template("forms.html")


if __name__ == '__main__':
    app.run(debug=True)
