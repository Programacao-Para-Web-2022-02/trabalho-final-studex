from studex import db

class users(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    usename = db.Column(db.String(15), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True )
    senha = db.Column(db.String(80), nullable=False)