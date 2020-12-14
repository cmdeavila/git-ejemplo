from wtforms import StringField
from flask_wtf import FlaskForm
from flask import Flask, render_template, request, redirect, url_for, flash
import os
from forms import FormInicio

app = Flask(__name__)
app.secret_key = os.urandom( 24 )

@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/login',methods=['GET', 'POST'])
def login():
  form = FormInicio()
  if(form.validate_on_submit()):
    flash('Inicio de sesión solicitado por el usuario {}, recordar={}'
          .format(form.usuario.data, form.recordar.data))
    return redirect(url_for('gracias'))
  return render_template('iniciar_sesion.html', form=form)
@app.route('/gracias')
def gracias():
   return render_template('gracias.html')

if __name__ == "__main__":
    app.run(debug = True, port=8000)
    