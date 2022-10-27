from studex import db

class users(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(15), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True )
    senha = db.Column(db.String(80), nullable=False)
    nome = db.Column(db.String(120), nullable=False)
    ra = db.Column(db.String(12), nullable=False)
    tempo_prog = db.Column(db.String(15), nullable=False)
    ling_pref = db.Column(db.String(80), nullable=False)
    sis_op = db.Column(db.String(80), nullable=False)
    nivel_py = db.Column(db.String(), nullable=False)
    nivel_js = db.Column(db.String(), nullable=False)
    nivel_c = db.Column(db.String(), nullable=False)
    nivel_htmlcss = db.Column(db.String(), nullable=False)
    nivel_java = db.Column(db.String(), nullable=False)
    resumo = db.Column(db.String(500), nullable=False)


class forms(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    cod_email = db.Column(db.Integer, primary_key=True)
        