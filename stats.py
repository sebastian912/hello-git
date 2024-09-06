import json

data = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Medellin"
}

with open("datos.json", "w") as file:
    json.dump(data, file, indent=4)