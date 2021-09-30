from flask import Flask
from flask import request
app = Flask(__name__)
@app.route('/') 
def index():
    return "Ciclo 3. Desarrollo Web"

@app.route('/saluda') 
def saludarh():
    return 'Hola Grupo'

@app.route('/saluda/nuevo') 
def nuevo1():
    return 'Hola Grupo nuevo'

#params?parametro1=xxxxx&parametro2=yyyy
@app.route('/params') 
def parametros():
    param = request.args.get('params1', 'No contiene parametro')
    param_dos = request.args.get('params2', 'No contiene parametro dos')
    
    #return 'El parametro es: {}'.format(param)
    return 'El parametro es: {} {}'.format(param, param_dos)

if __name__ == '__main__':
    app.run(debug = True, port=8000)