from flask import Flask
from datetime import timedelta
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.app_context().push()
app.secret_key = "studex"
app.config['SECRET_KEY'] = 'studexmaiordetodos#tomatomatoma##kjkjkjkjkj'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///studex.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#app.permanent_session_lifetime = timedelta(minutes=5)
Bootstrap(app)
db = SQLAlchemy(app)

from studex import routes



