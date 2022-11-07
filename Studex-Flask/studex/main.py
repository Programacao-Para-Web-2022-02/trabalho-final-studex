from flask import redirect, url_for, render_template, request, Blueprint
# from studex.forms import Form, LoginForm
from studex import create_app, db
from studex.Models.Usuario import Usuario
from studex.Services.LoginServices import logincheckout
from studex.DAO.FormDAO import form_add_user


app = create_app()
principal = Blueprint('main', __name__)


@app.route('/')
def home():
    return render_template("forms.html")

# Login


@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    logincheckout(form)

    return render_template("login.html", form=form)


@app.route("/form", methods=["POST", "GET"])
def form():
    form = Form()
    form_add_user(form, request.method)
    return render_template("form.html", form=form)


@app.route("/forms", methods=["POST", "GET"])
def forms():
    if request.method == "POST":
        new_user = Usuario(
                        usuario=request.form["nm"],
                        email= request.form["em"],
                        senha=request.form["pss"],
                        ra=request.form["ra"],
                        semestre=request.form["se"],
                        tempo=request.form["tm"],
                        linguagem=request.form["lg"],
                        so=request.form["so"],
                        python=request.form["py"],
                        javascript=request.form["js"],
                        c=request.form["c"],
                        html=request.form["html"],
                        java=request.form["jv"],
                        resumo=request.form["rs"])

        db.session.add(new_user)
        db.session.commit()
        return f'<h1>Novo Usuário foi criado <br> Todos os Usuario = {Usuario.query.all()}<br> !</h1> '

    return render_template("forms.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
