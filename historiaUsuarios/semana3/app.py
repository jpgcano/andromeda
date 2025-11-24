from servicios import (
    agregar_producto,
    mostrar_inventario,
    buscar_producto,
    actualizar_producto,
    eliminar_producto,
    calcular_estadisticas,
)
from archivos import guardar_cvs, cargar_csv

# Lista que almacenará los productos en memoria. Cada producto es un diccionario
# con claves como "nombre", "precio" y "cantidad".
inventario = []

# Bandera para controlar la ejecución del bucle principal del menú.
flag = True


# Bucle principal: muestra el menú y procesa la opción seleccionada por el usuario.
while flag:
    # Mensaje de bienvenida y menú de opciones.
    print("""
            ------------------------------------------------------
                                  Bienvenidos
                                MENÚ PRINCIPAL
            ------------------------------------------------------

                        Selecciona una opción del 1 al 9:
                        [1] - Agregar
                        [2] - Mostrar
                        [3] - Buscar
                        [4] - Actualizar
                        [5] - Eliminar
                        [6] - Estadísticas
                        [7] - Guardar CSV
                        [8] - Cargar CSV
                        [9] - Salir
""")

    # Validación y manejo de la opción ingresada.
    try:
        menu = int(input("=>:  "))
        match menu:
            case 1:
                # Agregar un nuevo producto al inventario.
                try:
                    # Se capturan y normalizan los datos de entrada.
                    nombre = input("Ingrese nombre del producto:  ").strip().lower()
                    precio = float(input("ingrese precio del producto:   "))
                    cantidad = int(input("Ingrese la cantidad del producto:   "))

                    # Llamada a la lógica que crea la estructura del producto.
                    producto = agregar_producto(inventario, nombre, precio, cantidad)

                    # Si la función retorna un diccionario, el producto fue creado
                    # y se agrega al inventario en memoria; si retorna None, ya
                    # existía y no se duplica.
                    if producto is not None:
                        inventario.append(producto)
                        print("Se ingreso el producto con exito: ")
                    else:
                        print("El producto ya existe")
                except ValueError:
                    # Captura errores de conversión (float/int) en la entrada.
                    print("Error al ingresar Producto")

            case 2:
                # Mostrar todos los productos si existen.
                if inventario:
                    mostrar_inventario(inventario)
                else:
                    print("Sin inventario")

            case 3:
                # Buscar y mostrar un producto por nombre.
                try:
                    nombre = input("Ingrese nombre del producto:  ").strip().lower()
                    buscar_producto(inventario, nombre)
                except ValueError:
                    print("Error al Actualizar producto")

            case 4:
                # Actualizar precio y cantidad de un producto existente.
                try:
                    nombre = input("Ingresa nombre del producto:    ").strip().lower()
                    nuevo_precio = float(input("Ingresa el nuevo precio:  "))
                    nueva_cantidad = int(input("Ingresa la cantidad nueva:  "))

                    producto = actualizar_producto(
                        inventario, nombre, nuevo_precio, nueva_cantidad
                    )

                    # La función `actualizar_producto` puede retornar varios tipos:
                    # - None: producto no encontrado
                    # - str: mensaje indicando estado (por ejemplo, inventario vacío)
                    # - dict: el producto actualizado
                    if producto is None:
                        print("Producto no encontrado.")
                    elif isinstance(producto, str):
                        print(producto)  # Es el mensaje "Inventario vacío!"
                    else:
                        print("Producto actualizado:", producto)
                except ValueError:
                    print("Valor ingreado no valido")

            case 5:
                # Eliminar un producto por nombre.
                nombre = input("Ingresa nombre del producto a eliminar: ").strip().lower()
                resultado = eliminar_producto(inventario, nombre)
                if resultado is True:
                    print("Producto eliminado con éxito.")
                elif resultado is None:
                    print("Producto no encontrado.")
                else:
                    # `resultado` puede ser un mensaje cuando el inventario está vacío.
                    print(resultado)

            case 6:
                # Calcular y mostrar estadísticas del inventario.
                estadisticas = calcular_estadisticas(inventario)
                if isinstance(estadisticas, str):
                    # Mensaje devuelto cuando no hay datos suficientes.
                    print(estadisticas)
                else:
                    print("\n--- Estadísticas del Inventario ---")
                    print("Total de productos:", estadisticas["total_productos"])
                    print("Valor total del inventario:", estadisticas["valor_total"])
                    print("Producto más caro:", estadisticas["producto_mas_caro"])
                    print("Producto con mayor stock:", estadisticas["producto_mayor_stock"])

            case 7:
                # Guardar el inventario actual en un archivo CSV.
                guardar_cvs(inventario, "inventaio.csv")

            case 8:
                # Cargar productos desde un CSV. La función retorna un dict con
                # listas de productos válidos y la cuenta de errores.
                resultado = cargar_csv("inventaio.csv")
                if isinstance(resultado, str):
                    # Si la función retorna una cadena, se trata de un mensaje de error.
                    print(resultado)
                    continue
                cargados = resultado["productos"]
                errores = resultado["errores"]
                if not cargados:
                    print("No se cargaron productos válidos.")
                    continue
                print(f"Se encontraron {len(cargados)} productos válidos.")
                if errores > 0:
                    print(f"{errores} filas inválidas fueron omitidas.")
                # Pregunta si se sobrescribe el inventario actual o se fusionan.
                decision = input("¿Sobrescribir inventario actual? (S/N): ").strip().lower()
                if decision == "s":
                    inventario = cargados
                    print("Inventario reemplazado completamente.")
                else:
                    # Política de fusión: si el producto ya existe, sumar cantidades
                    # y actualizar el precio con el del archivo cargado; sino, añadir.
                    print("Fusión activada: actualizando productos existentes.")
                    for nuevo in cargados:
                        for item in inventario:
                            if item["nombre"] == nuevo["nombre"]:
                                item["cantidad"] += nuevo["cantidad"]
                                item["precio"] = nuevo["precio"]
                                break
                        else:
                            inventario.append(nuevo)
                    print("Fusión completada.")
                print("Inventario actualizado:")
                mostrar_inventario(inventario)
            case 9:
                # Salir del bucle y terminar el programa.
                flag = 0

            case _:
                # Opción no válida
                print("Ingrese opción valida entre el 1 al 9")

    except ValueError:
        # Manejo de entrada no numérica para el menú.
        print("Solo se permiten números")
    except IOError as e:
        # Captura de errores de I/O no específicos.
        print("Otro error", e)