import json
import os

ARCHIVO = "banco.json"

def cargar_datos():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, 'r') as file:
            return json.load(file)
    return {"usuarios": []}

def guardar_datos(datos):
    with open(ARCHIVO, 'w') as file:
        json.dump(datos, file, indent=4)

def buscar_usuario(datos, id_usuario):
    for user in datos["usuarios"]:
        if user["id"] == id_usuario:
            return user
    return None
