import os
import random
import yagmail as yagmail
from flask import Flask, render_template, request, flash, session, send_file, url_for,redirect
from formulario import formEstudiante, formLogin
import sqlite3
from markupsafe import escape
import hashlib
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/", methods=['GET', 'POST'])
def home():
    form = formEstudiante()
    return render_template("estudiantes.html" ,form = form)

#La lógica aplicada es la misma para forgot password.
@app.route("/activate", methods=["GET"])
def activate():
    # Este recibe los datos en la url, es decir por get
    tok = request.args.get('auth')
    # Se busca el usuario al que corresponde el token
    with sqlite3.connect("estudiantes.db") as con:
        con.row_factory = sqlite3.Row # convierte la resuesta de la Bd en un diccionario
        cur = con.cursor()
        cur.execute(f"SELECT Estudiantes.documento FROM Estudiantes INNER JOIN activationlink ON email=correo WHERE challenge = '{tok}'")
        #cur.execute("SELECT Estudiantes.documento FROM Estudiantes INNER JOIN activationlink ON email=correo WHERE challenge = ?",[tok])
        row = cur.fetchone()
        if row is None:
            sal = 'Token o enlace de activación no válido'
        else:
            doc = row[0]
            cur.execute("UPDATE Estudiantes SET estado=? WHERE documento=?",(1, doc))
            cur.execute(f"DELETE FROM activationlink WHERE challenge='{tok}'")
            #cur.execute("DELETE FROM activationlink WHERE challenge=?", [tok])
            con.commit() #confirma la sentencia
            sal = redirect(url_for('login'))
    return sal        

@app.route("/estudiante/save", methods=["POST"])
def estudiante_save():
    if "usuario" in session:
        form = formEstudiante()
        if request.method == "POST":
            documento = form.documento.data
            nombre = form.nombre.data
            correo = form.correo.data
            sexo = form.sexo.data
            ciclo = form.ciclo.data
            estado = form.estado.data
            f = request.files['archivo']
            f.save(f.filename)
            #try:
            with sqlite3.connect("estudiantes.db") as con:
                cur = con.cursor() #Manipula la conexión a la bd
                cur.execute("INSERT INTO Estudiantes (documento, nombre, sexo, ciclo, estado, correo, ruta) VALUES (?,?,?,?,?,?,?)",
                            (documento, nombre, sexo, ciclo, estado, correo,f.filename))
                con.commit() #confirma la sentencia
                
                number = hex(random.getrandbits(512))[2:]
                
                
                cur.execute(
                        'INSERT INTO activationlink(challenge, state, documento,email) VALUES (?,?,?,?)',
                        (number,0, documento,correo)
                    )
                con.commit()
                yag = yagmail.SMTP(user="pruebamintic2022@gmail.com", password="Jmd12345678") #user correo
                yag.send(to=correo, subject='Activa tu cuenta', contents='Bienvenido, usa este link para activar tu cuenta '+url_for('activate',_external=True)+'?auth='+number )
                return "Se guardo satisfactoriamente"
            # except :
            #     con.rollback()
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
    
    usuario = escape(request.form["usuario"])
    contrasena = escape(request.form["contrasena"])

    with sqlite3.connect("estudiantes.db") as con:
        try:
            cur = con.cursor()
            #user=cur.execute(f"SELECT clave FROM usuario WHERE usuario ='{usuario}'").fetchone()
            user=cur.execute("SELECT clave FROM usuario WHERE usuario =?",[usuario]).fetchone()
            if user != None:
                clave = user[0]
                
                if check_password_hash(clave, contrasena):
                    #if cur.fetchone():
                        session["usuario"] = usuario #Creo la variable de sesion
                        form = formEstudiante()
                        return render_template("estudiantes.html", form=form)
                        flash (user)
                else:
                        return 'Usuario o contraseña inválidos'       
            else:
                return 'Usuario o contraseña inválidos'
        
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
        # encrip=hashlib.md5(contrasena.encode())
        # consenc=encrip.hexdigest()
        hashContraseña = generate_password_hash(contrasena)
        with sqlite3.connect("estudiantes.db") as con:
            try:
                cur = con.cursor()
                # cur.execute("INSERT INTO usuario (usuario, clave) VALUES (?,?)",
                #             (usuario, contrasena))
                # cur.execute("INSERT INTO usuario (usuario, clave) VALUES (?,?)",
                #             (usuario, consenc))
                cur.execute("INSERT INTO usuario (usuario, clave) VALUES (?,?)",
                            (usuario, hashContraseña))
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

@app.route( '/downloadpdf', methods=('GET', 'POST') )
def downloadpdf():
    return send_file( "resources/doc.pdf", as_attachment=True )


@app.route( '/downloadimage', methods=('GET', 'POST') )
def downloadimage():
    return send_file( "resources/image.png", as_attachment=True )

@app.route('/uploader/',methods=['POST'])
def uploader():
    f = request.files['fload']
    f.save(f.filename)
    return 'file uploaded successfully'

if __name__=='__main__':
    app.run( host='127.0.0.1', port =443, ssl_context=('micertificado.pem', 'llaveprivada.pem')  )
