import os
from flask import Flask, render_template, request, flash, session
from formulario import formEstudiante, formLogin
import sqlite3
from markupsafe import escape
import hashlib

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/", methods=['GET', 'POST'])
def home():
    form = formEstudiante()
    return render_template("estudiantes.html" ,form = form)

@app.route("/estudiante/save", methods=["POST"])
def estudiante_save():
    if "usuario" in session:
        form = formEstudiante()
        if request.method == "POST":
            documento = form.documento.data
            nombre = form.nombre.data
            sexo = form.sexo.data
            ciclo = form.ciclo.data
            estado = form.estado.data
            try:
                with sqlite3.connect("estudiantes.db") as con:
                    cur = con.cursor() #Manipula la conexión a la bd
                    cur.execute("INSERT INTO Estudiantes (documento, nombre, sexo, ciclo, estado) VALUES (?,?,?,?,?)",
                                (documento, nombre, sexo, ciclo, estado))
                    con.commit() #confirma la sentencia
                    return "Se guardo satisfactoriamente"
            except :
                con.rollback()
        return "No se pudo guardar"
    else:
        return "Acción no permitida <a href = '/login' > Login </a>"

@app.route("/estudiante/get",  methods=["GET", "POST"])
def estudiante_get():
    if "usuario" in session:
        form = formEstudiante()
        if request.method == "POST":
            doc = form.documento.data
            with sqlite3.connect("estudiantes.db") as con:
                try:
                    con.row_factory = sqlite3.Row # convierte la resuesta de la Bd en un diccionario
                    cur = con.cursor()
                    cur.execute("SELECT * FROM Estudiantes WHERE documento = ?", [doc] )
                    row = cur.fetchone()
                    if row is None:
                        flash("Estudiante no se encuentra en la BD")
                    return render_template("vista_estudiante.html", row=row)
                except:
                    con.rollback()
        return "Error en el Método"
    else:
        return "Acción no permitida <a href = '/login' > Login </a>"

@app.route("/estudiante/list", methods=["GET", "POST"]) 
def estudiante_list():
    if "usuario" in session:
        try:
            with sqlite3.connect("estudiantes.db") as con:
                    con.row_factory = sqlite3.Row # convierte la resuesta de la Bd en un diccionario
                    cur = con.cursor()
                    cur.execute("SELECT * FROM Estudiantes" )
                    row=cur.fetchall()
                    return render_template("lista_estudiante.html", row = row)
        except:
            return " No listado"  
    else:
        return "Acción no permitida <a href = '/login' > Login </a>"       

@app.route('/estudiante/delete', methods=["POST"])
def estudiante_delete():
    if "usuario" in session:
        form = formEstudiante()
        documento = form.documento.data
        with sqlite3.connect("estudiantes.db") as con:
            try:
                cur = con.cursor()
                cur.execute("DELETE FROM Estudiantes WHERE documento = ?", [documento])
                if con.total_changes > 0:
                    mensaje =  'Estudiante borrado'
                else:
                    mensaje =  'Estudiante no encontrado'
                
            except:
                mensaje =  'Ocurrió un error al borrar el estudiante'
                con.rollback()
            finally:
                return mensaje
    else:
        return "Acción no permitida <a href = '/login' > Login </a>"     
@app.route('/estudiante/update', methods=['POST'])
def estudiante_update():
    if "usuario" in session:
        form = formEstudiante()
        documento = form.documento.data
        nombre = form.nombre.data
        ciclo = form.ciclo.data
        sexo = form.sexo.data
        estado = form.estado.data

        with sqlite3.connect("estudiantes.db") as con:
            try:
                cur = con.cursor()
                cur.execute("UPDATE Estudiantes SET nombre = ?, ciclo = ?, sexo = ?, estado = ? WHERE documento = ?; ", [nombre,ciclo,sexo,estado,documento])
                con.commit()
                if con.total_changes > 0:
                    mensaje =  'Estudiante actualizado'
                else:
                    mensaje =  'Estudiante no encontrado'
                
            except:
                mensaje = 'Ocurrió un error al actualizar el estudiante'
                con.rollback()
            finally:
                return mensaje
    else:
        return "Acción no permitida <a href = '/login' > Login </a>"  

#Inyección SQL

@app.route('/login')
def login():
    form = formLogin()
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login_post():
    form = formEstudiante()
    usuario = request.form["usuario"]
    contrasena = request.form["contrasena"]

    with sqlite3.connect("estudiantes.db") as con:
        try:
            cur = con.cursor()
            #cur.execute("SELECT * FROM usuario WHERE usuario = '"+ usuario +"' AND clave = '"+ contrasena +"'")
            cur.execute("SELECT * FROM usuario WHERE usuario = ? AND clave = ? ", [usuario, contrasena])
            if cur.fetchone():
                session["usuario"] = usuario #Creo la variable de sesion
                #return 'Usuario logeado'
                return render_template("estudiantes.html", form=form)
                
    
        except:
            con.rollback()
    return 'Usuario no permitido'

#Inyección CODIGO
@app.route('/inyeccion')
def inyeccion():
    form = formLogin()
    return render_template("xss.html", form=form)

@app.route("/inyeccion", methods= ["POST"] )
def inyec():
    #usuario = request.form["usuario"]
    usuario = escape(request.form["usuario"])
    return usuario

#ENCRIPTAR
@app.route("/login/save",  methods= ["POST"])
def encriptar():
    form = formLogin()
    if request.method == "POST":
        usuario = request.form["usuario"]
        contrasena = request.form["contrasena"]
        encrip=hashlib.md5(contrasena.encode())
        consenc=encrip.hexdigest()
        
        with sqlite3.connect("estudiantes.db") as con:
            try:
                cur = con.cursor()
                # cur.execute("INSERT INTO usuario (usuario, clave) VALUES (?,?)",
                #             (usuario, contrasena))
                cur.execute("INSERT INTO usuario (usuario, clave) VALUES (?,?)",
                            (usuario, consenc))
                con.commit()
                return 'Guardado Satisfactoriamente'
            except:
                con.rollback()
        return ' No se puedo guardar' 

@app.route('/logout')
def logout():
    if 'usuario' in session:
        session.pop('usuario', None)
        return render_template('logout.html')
    else:
        return '<p> El usuario ya ha cerrado la sesión </p>   '

if __name__=='__main__':
    app.run (debug=True, port=8080)
