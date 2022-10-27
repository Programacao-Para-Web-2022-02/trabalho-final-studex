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
    email = StringField('E-mail: ', validators=[InputRequired(), Email(message='Email Inválido'), Length(max=50)])
    username = StringField('Usuário: ', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Senha: ', validators=[InputRequired(), Length(min=6, max=80)])

    def validate_username(self, username):
            usuario = users.query.filter_by(usename=username.data).first()
            if usuario:
                raise ValidationError("Esse usuario já foi cadastrado. Tente usar outro nick para continuar")


    def validate_email(self, email):  
        usuario = users.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError("Esse E-mail já foi cadastrado. Tente usar outro e-mail para continuar")


class Form(FlaskForm):
    email = StringField('E-mail: ', validators=[InputRequired(), Email(message='Email Inválido'), Length(max=50)])
    username = StringField('Usuário: ', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Senha: ', validators=[InputRequired(), Length(min=6, max=80)])
    nome = StringField('Nome: ', validators=[InputRequired(), Length(max=120)])
    ra = StringField('RA: ', validators=[InputRequired(), Length(max=12)])
    tempo_prog = StringField('Tempo de Programação: ', validators=[InputRequired(), Length(max=15)])
    ling_pref = StringField('Linguagem de Programação preferida: ', validators=[InputRequired(), Length(max=80)])
    sis_op = StringField('Sistema Operacional preferido: ', validators=[InputRequired(), Length(max=80)])
    nivel_py = StringField('Nivel de Conhecimento em Python: ', validators=[InputRequired()])
    nivel_js = StringField('Nivel de Conhecimento em JavaScript', validators=[InputRequired()])
    nivel_c = StringField('Nivel de Conhecimento em C:', validators=[InputRequired()])
    nivel_htmlcss = StringField('Nivel de Conhecimento em  HTML/CSS:', validators=[InputRequired()])
    nivel_java = StringField('Nivel de Conhecimento em Java: ', validators=[InputRequired()])
    resumo = StringField('Resumo Pessoal: ', validators =[InputRequired(), Length(min=5, max=500)])




    def validate_username(self, username):
            usuario = users.query.filter_by(usename=username.data).first()
            if usuario:
                raise ValidationError("Esse usuario já foi cadastrado. Tente usar outro nick para continuar")


    def validate_email(self, email):  
        usuario = users.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError("Esse E-mail já foi cadastrado. Tente usar outro e-mail para continuar")

