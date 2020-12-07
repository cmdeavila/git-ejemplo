import os

import yagmail as yagmail
from flask import Flask, render_template, flash, request, redirect, url_for
import utils

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/')
def index():
    return render_template('register.html')


@app.route('/register', methods=('GET', 'POST'))
def register():
    try:
        if request.method == 'POST':
            username = request.form['usuario']
            password = request.form['password']
            email = request.form['email']
            error = None

            if not utils.isUsernameValid(username):
                error = "El usuario debe ser alfanumerico o incluir solo '.','_','-'"
                flash(error)
                return render_template('register.html')

            if not utils.isPasswordValid(password):
                error = 'La contraseña debe contenir al menos una minúscula, una mayúscula, un número y 8 caracteres'
                flash(error)
                return render_template('register.html')

            if not utils.isEmailValid(email):
                print("4")
                error = 'Correo invalido'
                flash(error)
                return render_template('register.html')

            yag = yagmail.SMTP('pruebamintic2022', 'Jmd12345678') #modificar con tu informacion personal
            yag.send(to=email, subject='Activa tu cuenta',
                     contents='Bienvenido, usa este link para activar tu cuenta ')
            flash('Revisa tu correo para activar tu cuenta')
            return render_template('login.html')
        print("Llego al final")
        return render_template('register.html')
    except:
        return render_template('register.html')
if __name__ == "__main__":
    app.run(debug = True, port=8000)
