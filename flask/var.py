from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return "Variables"

@app.route('/user')
@app.route('/user/<name>')
def user(name='carmen'):
    return render_template('user1.html')
if __name__ == '__main__':
    app.run(debug = True, port=8000)