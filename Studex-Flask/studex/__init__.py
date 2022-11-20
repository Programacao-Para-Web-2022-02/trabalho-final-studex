from flask import Flask, render_template
from datetime import timedelta
# from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from os import path

from flask_login import LoginManager
from flask_googlemaps import GoogleMaps



db = SQLAlchemy()
DB_NAME = 'Studex'
senha_db = '123456'


def create_app():
    app = Flask(__name__)
    app.app_context().push()
    app.secret_key = "studex"
    app.config['SECRET_KEY'] = 'studexmaiordetodos#tomatomatoma##kjkjkjkjkj'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:{senha_db}@localhost/Studex'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.config['GOOGLEMAPS_KEY'] = "AIzaSyD4c_798PtEHYjZBhkF1VN9PioH_4Cru8Y"
    GoogleMaps(app)
    GoogleMaps(app, key="AIzaSyD4c_798PtEHYjZBhkF1VN9PioH_4Cru8Y")

    # Bootstrap(app)
    db.init_app(app)

    # from studex.main import main
    # app.register_blueprint(main, url_prefix='/')

    from Models.Usuario import Usuario

    with app.app_context():
        db.create_all()

    from main import main

    app.register_blueprint(main, url_prefix='/')

    login_manager = LoginManager()
    login_manager.login_view = 'main.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id_user):
        return Usuario.query.get(int(id_user))

    return app

