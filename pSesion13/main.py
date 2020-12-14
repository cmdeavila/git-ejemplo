from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("login-get.html")

@app.route("/login", methods=["POST","GET"] )
def loginget():
    if request.method == "GET":
        user = request.args.get("username")
        password = request.args.get("password")
        if user == "carmen" and password =="123":
            return "Bienvenido: Inicio GET"
        else:
            return "Método no aceptado: GET"


@app.route("/form-post")
def main2():
    return render_template("login-post.html")

@app.route("/login/post", methods=["POST","GET"] )
def loginpost():
    if request.method == "POST":
        user = request.form["username"]
        password = request.form["password"]
        
        if user == "carmen" and password =="123":
            return "Bienvenido: Inicio POST"
        else:
            return "Método no aceptado: POST"

if __name__ == "__main__":
    app.run(debug=True, port=8000 )
