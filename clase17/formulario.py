from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired

class formEstudiante(FlaskForm):
    documento = StringField('Documento', validators=[DataRequired(message='No dejar vacio, completar')], render_kw={"placeholder":"Identificación"})
    nombre = StringField('Nombre', validators=[DataRequired(message='No dejar vacio, completar')], render_kw={"placeholder":"Nombres"})
    ciclo = SelectField('Ciclo', choices=[( 'Python' ),( 'Java' ), ( 'Web' )] )
    sexo = StringField('Sexo', validators=[DataRequired(message='No dejar vacio, completar')], render_kw={"placeholder":"M/F"})
    estado = BooleanField('Estado')
    enviar = SubmitField('Enviar', render_kw= {"onmouseover":"guardarEst()"})
    consultar = SubmitField('Consultar', render_kw= {"onmouseover":"consultarEst()"})
    listar = SubmitField('Listar', render_kw= {"onmouseover":"listarEst()"})
    borrar = SubmitField('Borrar', render_kw= {"onmouseover":"borrarEst()"})
    actualizar = SubmitField('Actualizar', render_kw= {"onmouseover":"actualizarEst()"})

class formLogin(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired(message='No dejar vacio, completar')], render_kw={"placeholder":"Digite el nombre de usuario"})
    contrasena = PasswordField('Contraseña', validators=[DataRequired(message='No dejar vacio, completar')], render_kw={"placeholder":"Digite la contraseña"})
    enviar = SubmitField('Enviar')
    insertar = SubmitField('Insertar')
    