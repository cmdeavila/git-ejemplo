from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField
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