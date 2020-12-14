from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class Estudiante( FlaskForm ):
    documento = StringField( 'Documento', validators=[DataRequired( message='No dejar vacío, completar' )] )
    nombre = StringField( 'Nombre', validators=[DataRequired( message='No dejar vacío, completar' )] )
    ciclo = SelectField(u'Ciclo', choices=[('py', 'Python'), ('java', 'Java'), ('html', 'Web')])
    sexo = StringField( 'Sexo', validators=[DataRequired( message='No dejar vacío, completar' )] )
    estado = BooleanField( 'Estado')
    enviar = SubmitField( 'Enviar' )
