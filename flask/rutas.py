from flask import Flask
from flask import request
app = Flask(__name__)
@app.route('/') 
def index():
    return 'Hola mundo 8000'

@app.route('/saluda') 
def saluda():
    return 'Hola Grupo 14'

#params?parametro1=xxxxx&parametro2=yyyy
@app.route('/params') 
def params():
    param = request.args.get('params1', 'No contiene parametro')
    param_dos = request.args.get('params2', 'No contiene parametro dos')
    
    return 'El parametro es: {} {}'.format(param, param_dos)

if __name__ == '__main__':
    app.run(debug = True, port=8000)