import json

try:
    with open('datos.json' , 'r') as archivo:
        # la funcipi load() paserialza el archivo (json a oython )
        datos_json = json.load(archivo)
        print("Tipo de dato cargado: ". type(datos_json))
except FileNotFoundError:
    print("archivo no encontrado    ")