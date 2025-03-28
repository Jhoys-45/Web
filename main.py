from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "¡Hola, Render! 🚀"}

@app.get("/saludo/{nombre}")
def read_item(nombre: str):
    return {"message": f"Hola, {nombre}!"}
