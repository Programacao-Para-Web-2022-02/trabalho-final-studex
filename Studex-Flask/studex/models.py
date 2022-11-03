from studex import db

class users(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(15), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True )
    senha = db.Column(db.String(80), nullable=False)
    ra = db.Column(db.String(12), nullable=False)
    semestre = db.Column(db.String(3), nullable=False)
    tempo = db.Column(db.String(15), nullable=False)
    linguagem = db.Column(db.String(80), nullable=False)
    so = db.Column(db.String(80), nullable=False)
    python = db.Column(db.String(), nullable=False)
    javascript = db.Column(db.String(), nullable=False)
    c = db.Column(db.String(), nullable=False)
    html = db.Column(db.String(), nullable=False)
    java = db.Column(db.String(), nullable=False)
    resumo = db.Column(db.String(500), nullable=False)

class forms(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    cod_email = db.Column(db.Integer, primary_key=True)
        