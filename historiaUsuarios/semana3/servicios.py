"""Funciones de negocio para gestionar un inventario en memoria.

Cada producto se representa como un diccionario con las claves:
- "nombre" (str)
- "precio" (float)
- "cantidad" (int)

Las funciones esperan recibir la lista `inventario` (lista de dicts)
y realizan operaciones de consulta y modificación sobre ella.
"""

def agregar_producto(inventario, nombre, precio, cantidad):
    """Crear un producto si no existe y retornarlo.

    Parámetros:
    - inventario: lista de productos (mutuable)
    - nombre: nombre del producto (str)
    - precio: precio unitario (float)
    - cantidad: cantidad disponible (int)

    Retorna:
    - dict: producto creado
    - None: si el producto ya existe en el inventario
    """
    # Verificar si ya existe un producto con el mismo nombre
    item = buscar_producto(inventario, nombre)
    if item is not None:
        return None

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
    }
    return producto


def mostrar_inventario(inventario):
    """Imprime por consola una representación legible del inventario.

    Recorre cada producto en la lista e imprime su nombre, precio y
    cantidad en un formato fácil de leer.
    """
    for producto in inventario:
        print(
            f"""
            --------------------------------------------------
                --- Nombre:     {producto['nombre']}
                --- Precio:     {producto['precio']}
                --- Cantidad:   {producto['cantidad']}
            --------------------------------------------------"""
        )


def buscar_producto(inventario, nombre):
    """Buscar un producto por su `nombre` en la lista `inventario`.

    Retorna el diccionario del producto si se encuentra, o `None` si no.
    """
    for item in inventario:
        if item["nombre"] == nombre:
            return item
    return None


def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """Actualizar precio y/o cantidad de un producto existente.

    Si `inventario` está vacío retorna un mensaje indicando el estado.
    Si el producto no se encuentra retorna `None`.
    Si se encuentra, actualiza los campos no-None y retorna el producto modificado.
    """
    if not inventario:
        return "¡Inventario vacío!"

    for item in inventario:
        if item["nombre"] == nombre:
            if nuevo_precio is not None:
                item["precio"] = nuevo_precio
            if nueva_cantidad is not None:
                item["cantidad"] = nueva_cantidad
            return item

    return None


def eliminar_producto(inventario, nombre):
    """Eliminar un producto del inventario por nombre.

    Retorna True si se eliminó con éxito, None si no se encontró, o un
    mensaje (str) si el inventario está vacío.
    """
    if not inventario:
        return "¡Inventario vacío!"

    for index, item in enumerate(inventario):
        if item["nombre"] == nombre:
            del inventario[index]
            return True

    return None


def calcular_estadisticas(inventario):
    """Calcular métricas útiles sobre el inventario.

    Devuelve un diccionario con:
    - total_productos: número de ítems en el inventario
    - valor_total: suma del (precio * cantidad) de todos los productos
    - producto_mas_caro: el dict del producto con mayor precio
    - producto_mayor_stock: el dict del producto con mayor cantidad

    Si el inventario está vacío retorna un mensaje (str).
    """
    if not inventario:
        return "Inventario vacío"

    totalProductos = len(inventario)
    valorTotal = sum(item["precio"] * item["cantidad"] for item in inventario)

    # Producto con mayor precio
    masCaro = max(inventario, key=lambda x: x["precio"])

    # Producto con mayor cantidad (stock)
    masStock = max(inventario, key=lambda x: x["cantidad"])

    return {
        "total_productos": totalProductos,
        "valor_total": valorTotal,
        "producto_mas_caro": masCaro,
        "producto_mayor_stock": masStock,
    }