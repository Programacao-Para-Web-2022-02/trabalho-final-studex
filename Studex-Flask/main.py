from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route("/form", methods=["POST", "GET"])
def form():
    if request.method == "POST":
        user = request.form["nm"]
        ra = request.form["ra"]
        semestre = request.form["se"]
        tempo = request.form["tm"]
        linguagem = request.form["lg"]
        so = request.form["so"]
        python = request.form["py"]
        javascript = request.form["js"]
        c = request.form["c"]
        html = request.form["html"]
        java = request.form["jv"]
        resumo = request.form["rs"]
        return redirect(url_for("user", usr=[user, ra, semestre, tempo, linguagem, so, python, javascript, c, html, java, resumo]))
    else:
        return render_template("form.html", content="forms")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"


if __name__ == "__main__":
    app.run(debug=True)