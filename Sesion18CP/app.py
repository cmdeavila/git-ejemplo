import os

from flask import Flask, render_template, flash, request, redirect, url_for, jsonify
from db import get_db

app = Flask( __name__ )
app.secret_key = os.urandom( 24 )


@app.route( '/' )
def index():
    return render_template( 'register.html' )


@app.route( '/register', methods=('GET', 'POST') )
def register():
    # try:
    if request.method == 'POST':
        username = request.form['usuario']
        password = request.form['password']
        email = request.form['email']
        error = None
        db = get_db()
        db.executescript(
            "INSERT INTO usuario (usuario, correo, contraseña) VALUES ('%s','%s','%s')" % (username, email, password)
            #"; UPDATE usuario set correo='hack';"
        )
        #db.execute(
        #    'INSERT INTO usuario (usuario, correo, contraseña) VALUES ('%s','%s','%s')' %
        #    (username, email, password)
        #)
        db.commit()
        print( "P2" )
        return render_template( 'register.html' )
    return render_template( 'register.html' )


# except:
#    return render_template( 'register.html' )

if __name__ == '__main__':
    app.run()
