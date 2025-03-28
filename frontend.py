# main.py (Backend con FastAPI)

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

# Montar archivos estáticos (CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Cargar HTML desde la carpeta templates
templates_path = Path("templates")

@app.get("/", response_class=HTMLResponse)
def home():
    """Devuelve la página principal HTML"""
    with open(templates_path / "index.html", "r", encoding="utf-8") as file:
        return file.read()

# Endpoint de prueba
@app.get("/api/hello")
def read_hello():
    """Devuelve un mensaje JSON de prueba"""
    return {"message": "Hola, esta es una API con FastAPI"}

# Frontend - index.html (Plantilla HTML)
html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web de Prueba</title>
    <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
    <h1>Bienvenido a mi web con FastAPI</h1>
    <button onclick="fetchHello()">Obtener Mensaje</button>
    <p id="message"></p>
    <script src="/static/script.js"></script>
</body>
</html>
"""

# Frontend - styles.css (CSS para estilos)
css_content = """
body {
    font-family: Arial, sans-serif;
    text-align: center;
    margin: 50px;
}
button {
    background-color: #007bff;
    color: white;
    padding: 10px 20px;
    border: none;
    cursor: pointer;
}
button:hover {
    background-color: #0056b3;
}
"""

# Frontend - script.js (JavaScript para interactividad)
js_content = """
function fetchHello() {
    fetch('/api/hello')
        .then(response => response.json())
        .then(data => {
            document.getElementById('message').innerText = data.message;
        });
}
"""
