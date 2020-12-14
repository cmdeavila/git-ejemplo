from flask import Flask, jsonify 
#jsonify convierte un objeto a un json típico del navegador 

app = Flask(__name__)

from articulos import articulos

@app.route('/')
@app.route('/api')
def api():
    return jsonify({"message":"Hola Mundo!"})

@app.route('/articulos')
def getArticulos():
    return jsonify({"articulos":articulos, 'message':"Listado de articulos"})

@app.route('/articulos/<string:nom_articulo>')
def getArticulo(nom_articulo):
    encontrado = [articulo for articulo in articulos
	if articulo['nombre']== nom_articulo] 
    if (len(encontrado) > 0):
  	    return jsonify({"articulo": encontrado[0]})
    return jsonify({"message":"Articulo no encontrado"})

#En el for, se recorre el listado de productos y va comparando hasta 
# encontrar el artículo solicitado
#En el if, se verifica si la longitud del objeto encontrado es mayor que 0

if __name__ == '__main__':
    app.run(debug=True, port=8000)
 
