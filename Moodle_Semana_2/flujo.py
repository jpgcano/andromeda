inventario = []

def agregar_producto():
    nombre = input("Ingresa el nombre del producto: ")

    try:
        precio = float(input("Ingresa el precio del producto: $"))
        cantidad = int(input("Ingrese la cantidad: "))

        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }

        inventario.append(producto)
        print(f"\nHas agregado {nombre} al inventario.")

    except ValueError:
        print("\ERROR: El precio o la cantidad deben ser valores numéricos válidos.")

def mostrar_inventario():
    # Muestra cada producto registrado en el inventario.
    if inventario:
        print("\n--- PRODUCTOS EN INVENTARIO ---") 

        for producto in inventario:
            print("="*36)
            print("Producto:")

            # Itera sobre las claves y valores del diccionario 'producto'
            for clave, valor in producto.items():
                print(f"{clave.capitalize()}: {valor}") 
            
        print("====================================\n")

    else:
        print("\nEl inventario está vacío.")

# --- 3. FUNCIÓN PARA CALCULAR ESTADÍSTICAS ---
def calcular_estadisticas():
    # Calcula y muestra el total de unidades y el valor total del inventario.
    if inventario:
        total_inventario = 0.0
        total_cantidad = 0

        for producto in inventario:
            total_cantidad += producto["cantidad"]
            valor_producto = producto["precio"] * producto["cantidad"]
            total_inventario += valor_producto

        print("\n--- ESTADÍSTICAS DEL INVENTARIO ---")
        print(f"Total de productos registrados: {total_cantidad} unidades")
        # Se usa formato de moneda para el valor total
        print(f"Valor total del inventario: ${total_inventario:,.2f}") 
        print("-----------------------------------\n")

    else:
        print("\nNo hay productos en el inventario para calcular estadísticas.")

# --- FUNCIÓN PRINCIPAL (MENÚ) ---
def menu_principal():
    """Gestiona el flujo principal del programa, mostrando el menú y llamando a las funciones."""
    print("---¡BIENVENIDO/A AL INVENTARIO!---")
    print("¿En qué te puedo ayudar?")

    while True:
        print("\n--MENÚ DE INVENTARIO--")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Calcular estadísticas")
        print("4. Salir")

        opcion = input("Elige una opción(1-4): ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            calcular_estadisticas()
        elif opcion == "4":
            print("\nGracias por utilizar el 'inventario'. ¡Hasta luego!")
            break
        else:
            print("\nError: Operación no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu_principal()

# COMENTARIO 18/11/25
