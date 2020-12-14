from flask import Flask 
from flask import render_template
from flask import request
app = Flask(__name__)

#Primera ruta para renderizar paginas 1-main.html y 2-main.html
@app.route('/')
def inicio():
    return render_template("index.html")

@app.route('/login', methods=["POST", "GET"])
def autenticar():
    nombre = request.form["nombre"]
    password = request.form["password"]
    if nombre == "carmen" and password == "123":
        return render_template("1-main.html", nombre=nombre)
    else:
        return render_template("2-main.html")

#Segunda ruta para renderizar paginas 3-ciclo.html
@app.route("/producto/list")
def product_list():
    productos = [{"nombre": "Yuca", "cantidad": 30},
                 {"nombre": "Ñame", "cantidad": 20},
                 {"nombre": "Papa", "cantidad": 15}]

    return render_template("3-ciclo.html", productos=productos)

#Tercera Ruta para renderizar paginas 4-plantillaH.html
#en esta ruta encuentras como ir de una página a otra por medio de botones
# y referencias <a href>
@app.route("/producto/save")
def product_save():
    return render_template("4-plantillaH.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000) 
