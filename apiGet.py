from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/saludo', methods=['GET'])
def saludo():
    # Obtenemos un parámetro opcional de la URL llamado "nombre"
    nombre = request.args.get('nombre', 'Mundo')
    # Retornamos un saludo personalizado o por defecto
    return jsonify({"mensaje": f"Hola, {nombre}!"})

if __name__ == '__main__':
    app.run(debug=True)
