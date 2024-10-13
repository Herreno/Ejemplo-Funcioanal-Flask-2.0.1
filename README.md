# API CRUD de Tareas en Flask

Esta es una API sencilla de tareas, creada con Flask, que permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre una lista de tareas.

## Requisitos

- Python 3.x
- Flask

## Instalación

1. Clona el repositorio o descarga los archivos.
2. Abre una terminal en el directorio del proyecto.
3. Instala los requisitos utilizando el siguiente comando:
   ```bash
   pip install -r requirements.txt
Uso
Inicia la aplicación ejecutando:
bash
python app.py
La aplicación se ejecutará en http://127.0.0.1:5000/.
Endpoints
Obtener todas las tareas
URL: /tareas
Método: GET
Descripción: Retorna la lista de todas las tareas.
Crear una nueva tarea
URL: /tareas
Método: POST
Body:
json
{
  "tarea": "Descripción de la tarea",
  "completado": false
}
Descripción: Crea una nueva tarea y la añade a la lista.
Actualizar una tarea existente
URL: /tareas/<id>
Método: PUT
Body:
json
{
  "tarea": "Tarea actualizada",
  "completado": true
}
Descripción: Actualiza la información de una tarea existente, donde <id> es el ID de la tarea.
Eliminar una tarea
URL: /tareas/<id>
Método: DELETE
Descripción: Elimina una tarea existente de la lista, donde <id> es el ID de la tarea.
Ejemplos de uso con curl
Crear una nueva tarea
bash
curl -X POST http://127.0.0.1:5000/tareas -H "Content-Type: application/json" -d '{"tarea": "Estudiar Flask", "completado": false}'
Obtener todas las tareas
bash
curl -X GET http://127.0.0.1:5000/tareas
Actualizar una tarea
bash
curl -X PUT http://127.0.0.1:5000/tareas/1 -H "Content-Type: application/json" -d '{"tarea": "Estudiar Flask más a fondo", "completado": true}'
Eliminar una tarea
bash
curl -X DELETE http://127.0.0.1:5000/tareas/1