from flask import Flask, request, jsonify

app = Flask(__name__)

# Método GET - Retorna un saludo
@app.route('/saludo', methods=['GET'])
def saludo_get():
    nombre = request.args.get('nombre', 'Mundo')
    return jsonify({"mensaje": f"Hola, {nombre}!"})

# Método POST - Envía un saludo usando un JSON en el cuerpo de la solicitud
@app.route('/saludo', methods=['POST'])
def saludo_post():
    data = request.get_json()  # Obtener datos en formato JSON del cuerpo de la solicitud
    nombre = data.get('nombre', 'Mundo')  # Si no se proporciona "nombre", se usa "Mundo"
    return jsonify({"mensaje": f"¡Saludos, {nombre} desde POST!"})

# Método PUT - Actualiza un saludo con datos enviados en el cuerpo de la solicitud
@app.route('/saludo', methods=['PUT'])
def saludo_put():
    data = request.get_json()
    nombre = data.get('nombre', 'Mundo')
    return jsonify({"mensaje": f"¡Saludos actualizados, {nombre} desde PUT!"})

# Método DELETE - Responde con un mensaje de eliminación
@app.route('/saludo', methods=['DELETE'])
def saludo_delete():
    return jsonify({"mensaje": "El saludo ha sido eliminado."})

if __name__ == '__main__':
    app.run(debug=True)
