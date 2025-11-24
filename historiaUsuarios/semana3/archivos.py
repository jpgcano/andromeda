"""Funciones utilitarias para leer y escribir inventarios en formato CSV.

Este módulo expone funciones para crear un CSV con encabezado, guardar
una lista de productos y cargar productos desde un CSV validando su
estructura y valores.
"""

import csv
import os


def crear_csv(ruta):
    """Crear un archivo CSV nuevo con el encabezado esperado.

    Si el archivo ya existe lo sobrescribe y escribe la primera fila con
    las columnas: nombre, precio, cantidad.
    """
    with open(ruta, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["nombre", "precio", "cantidad"])


def guardar_cvs(inventario, ruta):
    """Guardar una lista de productos en `ruta` (CSV).

    Parámetros:
    - inventario: lista de dicts con claves `nombre`, `precio`, `cantidad`
    - ruta: ruta del archivo CSV a escribir

    Retorna una cadena con la confirmación o un mensaje de error.
    """
    if not inventario:
        return "¡Inventario vacío!"

    # Si el archivo no existe, crear uno con encabezado para evitar mezclar
    # datos con archivos previos. Si existe, se abrirá en modo append.
    if not os.path.exists(ruta):
        crear_csv(ruta)

    try:
        with open(ruta, "a", newline="") as file:
            writer = csv.writer(file)
            for producto in inventario:
                writer.writerow(
                    [producto["nombre"], producto["precio"], producto["cantidad"]]
                )
        return "¡Inventario agregado correctamente!"

    except PermissionError:
        # Maneja errores de permiso
        print("Error: No tienes permisos para escribir en esta ubicación.")
    except IOError as e:
        # Maneja otros errores de entrada/salida genéricos
        print(f"Error de E/S al escribir el archivo: {e}")


def cargar_csv(ruta):
    """Cargar productos desde un CSV y validar su contenido.

    Retorna un diccionario con:
    - 'productos': lista de productos válidos (cada uno es un dict)
    - 'errores': número de filas inválidas que fueron ignoradas

    O retorna una cadena con un mensaje de error si falla la lectura/validación.
    """
    productos = []
    errores = 0

    if not os.path.exists(ruta):
        return "Archivo no encontrado."

    try:
        with open(ruta, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            encabezado = next(reader, None)

            # Validar encabezado exacto
            if encabezado != ["nombre", "precio", "cantidad"]:
                return "Encabezado inválido. Se esperaba: nombre,precio,cantidad"

            # Leer y validar cada fila
            for fila in reader:
                if len(fila) != 3:
                    errores += 1
                    continue
                nombre, precio, cantidad = fila
                try:
                    precio = float(precio)
                    cantidad = int(cantidad)
                    # Validar que no haya valores negativos
                    if precio < 0 or cantidad < 0:
                        errores += 1
                        continue
                    productos.append(
                        {
                            "nombre": nombre.strip().lower(),
                            "precio": precio,
                            "cantidad": cantidad,
                        }
                    )
                except ValueError:
                    errores += 1
                    continue

        resumen = {"productos": productos, "errores": errores}
        return resumen

    except UnicodeDecodeError:
        return "Error de codificación: el archivo no está en UTF-8."
    except Exception as e:
        return f"Error al leer CSV: {e}"