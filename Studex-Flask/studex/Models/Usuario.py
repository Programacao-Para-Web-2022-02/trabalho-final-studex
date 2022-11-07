from studex import db
from flask_login import UserMixin


class Usuario(db.Model, UserMixin):
    __table_args__ = {'extend_existing': True}
    _id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(15), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True )
    senha = db.Column(db.String(80), nullable=False)
    ra = db.Column(db.String(12), nullable=False)
    semestre = db.Column(db.String(3), nullable=False)
    tempo = db.Column(db.String(15), nullable=False)
    linguagem = db.Column(db.String(80), nullable=False)
    so = db.Column(db.String(80), nullable=False)
    python = db.Column(db.String(80), nullable=False)
    javascript = db.Column(db.String(80), nullable=False)
    c = db.Column(db.String(80), nullable=False)
    html = db.Column(db.String(80), nullable=False)
    java = db.Column(db.String(80), nullable=False)
    resumo = db.Column(db.String(500), nullable=False)
