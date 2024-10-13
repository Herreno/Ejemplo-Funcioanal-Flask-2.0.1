from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista de tareas de ejemplo
tareas = [
    {"id": 1, "tarea": "Comprar leche", "completado": False},
    {"id": 2, "tarea": "Llamar al presidente", "completado": True},
]

# Rutas
@app.route('/tareas', methods=['GET'])
def obtener_tareas():
    return jsonify(tareas)

@app.route('/tareas', methods=['POST'])
def agregar_tarea():
    nueva_tarea = request.get_json()
    nueva_tarea["id"] = len(tareas) + 1
    tareas.append(nueva_tarea)
    return jsonify(nueva_tarea), 201

@app.route('/tareas/<int:id>', methods=['PUT'])
def actualizar_tarea(id):
    tarea = next((t for t in tareas if t["id"] == id), None)
    if tarea is None:
        return jsonify({"error": "Tarea no encontrada"}), 404

    datos = request.get_json()
    tarea.update(datos)
    return jsonify(tarea)

@app.route('/tareas/<int:id>', methods=['DELETE'])
def eliminar_tarea(id):
    tarea = next((t for t in tareas if t["id"] == id), None)
    if tarea is None:
        return jsonify({"error": "Tarea no encontrada"}), 404

    tareas.remove(tarea)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
