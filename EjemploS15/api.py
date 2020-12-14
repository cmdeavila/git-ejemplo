import flask
from flask import request, jsonify

app = flask.Flask(__name__)


# Cree algunos datos de prueba para nuestro catálogo en forma de lista de diccionarios.
books = [
    {'id': 0,
     'title': 'Alan turing. El hombre que sabia demasiado',
     'author': 'David Leavitt',
     'first_sentence': 'El progenitor de las ideas que condujeron a la invención del ordenador.',
     'year_published': '2007'},
    {'id': 1,
     'title': 'Ready player one',
     'author': 'Ernest Cline',
     'first_sentence': 'El mundo es un desastre. Las fuentes de energía están prácticamente agotadas',
     'published': '2011'},
    {'id': 2,
     'title': 'El arte de la intrusión',
     'author': 'Kevin Mitnick',
     'first_sentence': 'Entra en el mundo hostil de los delitos informáticos desde la comodidad de tu propio sofá.',
     'published': '2005'}
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Archivo de lectura</h1>
<p>Un prototipo de API para la lectura de libros de tecnología.</p>'''

# Ruta para devolver todas las entradas disponibles en nuestro catálogo.
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

#http://127.0.0.1:8000/api/v1/resources/books?id=2
@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    # Verifique si se proporcionó una identificación como parte de la URL.
    # Si se proporciona un ID, asígnelo a una variable.
    # Si no se proporciona una identificación, muestra un error en el navegador.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No se proporcionó ningún campo de id. Especifique una id."

    # Crea una lista vacía para nuestros resultados
    results = []

    # Recorre los datos y haga coincidir los resultados que se ajusten al ID solicitado.
    # Los ID son únicos, pero otros campos pueden devolver muchos resultados
    for book in books:
        if book['id'] == id:
            results.append(book)

    # Utilice la función jsonify de Flask para convertir nuestra lista de
    # Diccionarios de Python al formato JSON.
    return jsonify(results)


if __name__ == "__main__":
    app.run(debug = True, port=8000)