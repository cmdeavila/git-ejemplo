from flask import Flask
app = Flask(__name__) #nuevo objeto
# Crear instancia de aplicación Flask con el nombre app. 
# Pasa la variable especial __name__ que contiene el nombre del módulo Pyhthon actual. 
# Se utiliza para indicar a la instancia dónde está ubicada. 
# Necesitará hacerlo porque Flask configura algunas rutas en segundo plano.

@app.route('/') #Decorador
# Decorador es el encargado  de  decirle  a Flask qué URL 
# debe ejecutar su correspondiente función

def index():
    return 'Hola mundo'
app.run()
# El nombre de la función será usado para generar internamente 
# URLs a partir de dicha función.
# Por último, la  función  retorna  la  respuesta  
# que  será  mostrada  en el navegador del usuario.
