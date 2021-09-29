from flask import Flask
from flask import render_template
app = Flask(__name__)
@app.route('/user')
@app.route('/user/<name>')
def user(name='carmen'):
    anios = 14
    lista = [1,2,3,4,5,6,7,8]
    return render_template('user.html', nombre=name, ani=anios, lis=lista)
if __name__ == '__main__':
    app.run(debug = True, port=8000)