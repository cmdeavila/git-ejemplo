from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class Login(FlaskForm):
    usuario = StringField('Usuario *', validators=[DataRequired(message='El campo usuario es requerido')])
    clave = PasswordField('Clave *', validators=[DataRequired(message='El campo clave es requerido')])
    enviar = SubmitField('Ingresar')

class Registro(FlaskForm):
    usuario = StringField('Usuario *', validators=[DataRequired(message='El campo usuario es requerido')])
    email = StringField('Email *', validators=[DataRequired(message='El campo usuario es requerido')])
    clave1 = PasswordField('Clave *', validators=[DataRequired(message='El campo clave es requerido')])
    clave2 = PasswordField('Verificación *', validators=[DataRequired(message='El campo clave es requerido')])
    enviar = SubmitField('Ingresar')    