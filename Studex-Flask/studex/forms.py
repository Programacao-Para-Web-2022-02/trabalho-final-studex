from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length, ValidationError
from studex.models import users
#import email_validator


class LoginForm(FlaskForm):
    username = StringField('usuário', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('senha', validators=[InputRequired(), Length(min=6, max=80)])
    remember = BooleanField('lembre de mim')


class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Email Inválido'), Length(max=50)])
    username = StringField('usuário', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('senha', validators=[InputRequired(), Length(min=6, max=80)])

    def validate_username(self, username):
            usuario = users.query.filter_by(usename=username.data).first()
            if usuario:
                raise ValidationError("Esse usuario já foi cadastrado. Tente usar outro nick para continuar")


    def validate_email(self, email):  
        usuario = users.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError("Esse E-mail já foi cadastrado. Tente usar outro e-mail para continuar")


