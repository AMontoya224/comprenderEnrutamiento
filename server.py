from flask import Flask

app = Flask(__name__)

@app.route("/")
def paginaInicial():
    return "Hola mundo!"

@app.route("/dojo")
def paginaDojo():
    return "¡Dojo!"

@app.route("/say/<nombre>")
def paginaSay(nombre):
    return f"Hola, {str(nombre)}!"

@app.route("/repeat/<numero>/<palabra>")
def paginaRepeat(numero, palabra):
    cadena = ""
    for i in range(0, int(numero)):
        cadena += f"<h3>{str(palabra)}</h3>"
    return cadena

@app.errorhandler(404)
def paginaNoEncontrada(error):
    return "¡Lo siento! No hay respuesta. Inténtalo mas tarde"

if __name__ == "__main__":
    app.run(debug=True)