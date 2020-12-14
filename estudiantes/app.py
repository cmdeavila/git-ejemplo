import os
from flask import Flask, render_template, request, flash
import sqlite3
from formularios import formEstudiante, formlogin
from markupsafe import escape
import hashlib

app = Flask(__name__)
app.secret_key = os.urandom( 24 )


@app.route("/",methods=['GET', 'POST'])
def home():
    form=formEstudiante()
    return render_template("estudiantes.html", form=form)

@app.route("/estudiante/save", methods=["POST"])
def estudiante_save():
    form = formEstudiante()
    if request.method == "POST":
        documento = form.documento.data
        nombre = form.nombre.data
        sexo = form.sexo.data
        ciclo = form.ciclo.data
        estado = form.estado.data
        try:
            with sqlite3.connect("estudiantes.db") as con:
                cur = con.cursor() #manipula la conexión a la bd
                cur.execute("INSERT INTO Estudiantes (documento,nombre,sexo,ciclo,estado) VALUES (?,?,?,?,?)",
                            (documento,nombre,sexo,ciclo,estado))
                con.commit()# confirma la transacción
                return 'Guardado satisfactoriamente'
        except:
            con.rollback()
    return 'No se pudo guardar'

@app.route("/estudiante/get", methods=["GET","POST"])
def estudiante_get(): 
    form = formEstudiante()
    if request.method == "POST":
        doc = form.documento.data
        try:
            with sqlite3.connect("estudiantes.db") as con:
                con.row_factory = sqlite3.Row #convierte la respuesta de la BD en un diccionario
                cur = con.cursor()
                cur.execute("SELECT * FROM Estudiantes WHERE documento = ?", [doc])
                row = cur.fetchone()
                if row is None:
                    flash ("Estudiante no se encuentra en Base de datos")
                return render_template("vista_estudiante.html", row = row)
        except:
            con.rollback()
    return 'Error en el método'

@app.route("/estudiante/list", methods=["GET","POST"])
def estudiante_list():
    try:
        with sqlite3.connect("estudiantes.db") as con:
            con.row_factory = sqlite3.Row #convierte la respuesta de la BD en un diccionario
            cur = con.cursor()
            cur.execute("SELECT * FROM Estudiantes")
            row = cur.fetchall()
            return render_template("lista_estudiante.html", row = row)
         
    except:
        return "No listado"

@app.route("/estudiante/delete", methods=["GET", "POST"])
def estudiante_delete():
    form = formEstudiante()
    documento = form.documento.data
    try:
        with sqlite3.connect("estudiantes.db") as con:
            cur = con.cursor()
            cur.execute(
                "DELETE FROM Estudiantes WHERE documento=?", [documento])
            if con.total_changes > 0:
                mensaje = "Estudiante Borrado!"
            else:
                mensaje = "Estudiante no encontrado"
    except:
        mensaje = "Error"
    finally:
        return mensaje

    return "No existe Estudiante"

@app.route("/estudiante/update", methods=["POST"])
def estudiante_update():
    form = formEstudiante()
    if request.method == "POST":
        documento = form.documento.data
        nombre = form.nombre.data
        sexo = form.sexo.data
        ciclo = form.ciclo.data
        estado = form.estado.data
        try:
            with sqlite3.connect("estudiantes.db") as con:
                cur = con.cursor()
                cur.execute("UPDATE Estudiantes  SET nombre = ?, ciclo = ?, sexo = ?, estado = ? WHERE documento = ?;", [
                            nombre, ciclo, sexo, estado, documento])
                con.commit()
                if con.total_changes > 0:
                    mensaje = "Estudiante Modificado"
                else:
                    mensaje = "Estudiante no se pudo modificar"
        except:
            con.rollback()
        finally:
            return mensaje

# Inyección de SQL
@app.route("/login")
def login1():
    form = formlogin()
    return render_template("login.html", form=form)

@app.route("/login", methods=["POST"])
def login():
    user = request.form["username"]
    password = request.form["password"]
    with sqlite3.connect("estudiantes.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM usuario WHERE usuario ='"+ user +"' AND clave = '"+ password +"'")
        cur.execute("SELECT * FROM usuario WHERE usuario = ? AND clave = ?", [user, password])
        if cur.fetchone():
            return "Usuario logueado"

    return "Usuario no permitido"

# Inyección de código

@app.route("/inyeccion-xss")
def inyeccion():
    form = formlogin()
    return render_template("XSS.html", form=form)


@app.route("/inyeccion-xss",methods=["POST"])
def inye_xss():
    usuario = request.form["cadena"]
    #usuario= escape(request.form["cadena"])
    return usuario

# Encriptar
#http://127.0.0.1:8000/login
@app.route("/login/save", methods=["POST"])
def encriptar():
    form = formlogin()
    if request.method == "POST":
        user = request.form["username"]
        password = request.form["password"]
        encrip=hashlib.md5(password.encode())
        consenc=encrip.hexdigest()
        try:
            with sqlite3.connect("estudiantes.db") as con:
                cur = con.cursor() 
                # cur.execute("INSERT INTO usuario (usuario,clave) VALUES (?,?)",
                #             (user,password))
                cur.execute("INSERT INTO usuario (usuario,clave) VALUES (?,?)",
                            (user,consenc))
                con.commit()# confirma la transacción
                return 'Guardado satisfactoriamente'
        except:
            con.rollback()
    return 'No se pudo guardar'

if __name__ == "__main__":
    app.run(debug = True, port=8000)