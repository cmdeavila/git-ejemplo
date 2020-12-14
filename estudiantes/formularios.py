from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class formEstudiante( FlaskForm ):
    documento = StringField( 'Documento', validators=[DataRequired( message='No dejar vacío, completar' )],render_kw={"placeholder": "Identificación"} )
    nombre = StringField( 'Nombre', validators=[DataRequired( message='No dejar vacío, completar' )],render_kw={"placeholder": "Nombres"} )
    ciclo = SelectField('Ciclo', choices=[('Python'), ('Java'), ( 'Web')])
    sexo = StringField( 'Sexo', validators=[DataRequired( message='No dejar vacío, completar' )],render_kw={"placeholder": "M/F"} )
    estado = BooleanField( 'Estado')
    enviar = SubmitField( 'Enviar',render_kw={"onmouseover": "guardarEst()"} )
    consultar = SubmitField( 'Consultar', render_kw={"onmouseover": "consultarEst()"})
    listar = SubmitField( 'Listar', render_kw={"onmouseover": "listarEst()"})
    eliminar = SubmitField( 'Eliminar', render_kw={"onmouseover": "eliminarEst()"})
    actualizar = SubmitField( 'Actualizar', render_kw={"onmouseover": "actualizarEst()"})

class formlogin(FlaskForm):
    usuario = StringField( 'Usuario', validators=[DataRequired( message='No dejar vacío, completar' )],render_kw={"placeholder": "Usuario"} )
    clave = PasswordField( 'Clave', validators=[DataRequired( message='No dejar vacío, completar' )],render_kw={"placeholder": "Contraseña"} )
    enviar = SubmitField( 'Enviar')   
    insertar = SubmitField( 'Insertar', render_kw={"onmouseover": "insertar()"})