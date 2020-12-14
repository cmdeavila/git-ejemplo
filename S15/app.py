import os
from flask import Flask, render_template, request
from formularios import Login, Registro
from markupsafe import escape  # Seguridad, evitar inyeccion HTML

app = Flask(__name__)
app.secret_key = os.urandom(24) # para ataques CSRF

@app.route('/')
@app.route('/login/',methods=["GET","POST"]) # [] --> Lista, () --> Tupla
def r_login():
    if request.method == 'POST':
        usr = escape(request.form['usuario'])
        pwd = escape(request.form['clave'])
        return f'{usr} su clave es {pwd}'
    else:
        nfrm = Login()
        return render_template('fLogin.html',form=nfrm)

@app.route('/registrar/',methods=["GET","POST"]) # [] --> Lista, () --> Tupla
def r_registro():
    if request.method == 'POST':
        usr = escape(request.form['usuario'])
        pwd = escape(request.form['clave1'])
        return f'{usr} su clave es {pwd}'
    else:
        nfrm = Registro()
        return render_template('fRegistro.html',form=nfrm)        