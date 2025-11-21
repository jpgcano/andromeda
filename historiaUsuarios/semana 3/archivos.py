import csv
def crear_csv(ruta):
    with open(ruta,"w",newline="") as file:
        writer = csv.writer(file)
        writer.writerow("nombre","precio","cantidad")

def guardar_csv(inventario, ruta, incluir_header=True):
    if len(inventario)==0:
        return "¡Inventario vacío!"
    if incluir_header:
        crear_csv(ruta)
    try:
        with open(ruta,"a",newline="") as file:
            writer = csv.writer(file)
            for producto in inventario:
                writer.writerow(producto["nombre"],producto["precio"],producto["cantidad"])
        return "¡Inventario agregado correctamente!"

    except PermissionError:
        # Maneja errores de permiso 
        print("Error: No tienes permisos para escribir en esta ubicación.")
    except IOError as e:
        # Maneja otros errores de entrada/salida genéricos
        print(f"Error de E/S al escribir el archivo: {e}")

def cargar_csv(ruta):
    return