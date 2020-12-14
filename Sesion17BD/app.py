import os
from flask import Flask, render_template, request, flash
from formulario import formEstudiante
import sqlite3

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/", methods=['GET', 'POST'])
def home():
    form = formEstudiante()
    return render_template("estudiantes.html" ,form = form)

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
                cur = con.cursor() #Manipula la conexión a la bd
                cur.execute("INSERT INTO Estudiantes (documento, nombre, sexo, ciclo, estado) VALUES (?,?,?,?,?)",
                            (documento, nombre, sexo, ciclo, estado))
                con.commit() #confirma la sentencia
                return "Se guardo satisfactoriamente"
        except :
            con.rollback()
    return "No se pudo guardar"

@app.route("/estudiante/get",  methods=["GET", "POST"])
def estudiante_get():
    form = formEstudiante()
    if request.method == "POST":
        doc = form.documento.data
        try:
            with sqlite3.connect("estudiantes.db") as con:
                con.row_factory = sqlite3.Row # convierte la resuesta de la Bd en un diccionario
                cur = con.cursor()
                cur.execute("SELECT * FROM Estudiantes WHERE documento = ?", [doc] )
                row = cur.fetchone()
                if row is None:
                    flash = ("Estudiante no se encuentra en la BD")
                return render_template("vista_estudiante.html", row=row)
        except:
            con.rollback()
    return "Error en el Método"

@app.route("/estudiante/list", methods=["GET", "POST"]) 
def estudiante_list():
    try:
        with sqlite3.connect("estudiantes.db") as con:
                con.row_factory = sqlite3.Row # convierte la resuesta de la Bd en un diccionario
                cur = con.cursor()
                cur.execute("SELECT * FROM Estudiantes" )
                row=cur.fetchall()
                return render_template("lista_estudiante.html", row = row)
    except:
        return " No listado"  
        

if __name__=='__main__':
    app.run (debug=True, port=8080)