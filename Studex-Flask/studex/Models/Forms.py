from __init__ import db


class Forms(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    cod_email = db.Column(db.Integer, primary_key=True)
