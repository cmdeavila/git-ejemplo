from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/') 
def index():
    name = 'Carmen'
    return render_template('index.html', nombre=name)

@app.route('/client') 
def client():
    lista_nombres = ['Rafael','Vanessa','Paola']
    return render_template('client.html', lista=lista_nombres)

if __name__ == '__main__':
    app.run(debug = True, port=8000)