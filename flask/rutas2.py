from flask import Flask
from flask import request
app = Flask(__name__)
@app.route('/') 
def index():
    return 'Hola equipo'
#params/libros/nombre
#params/libros/num
@app.route('/params/')
@app.route('/params/<nombre>')
@app.route('/params/<nombre>/<int:num>')
def params(nombre = 'No hay nombre', num = 'no hay número'):
    return 'El parametro es: {} {}'.format(nombre,num)

if __name__ == '__main__':
    app.run(debug = True, port=8000)