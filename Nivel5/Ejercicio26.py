# Ejercicio 26
carrito = []

print("Bienvenido al carrito. Ingresa 'salir' para terminar.")

while True:
    producto = input("Por favor ingresa un producto para agregar al carrito: ")

    if producto.lower() == 'salir':
        break

    precio = float(input(f"Por favor ingresa el precio del {producto}: $"))
    carrito.append(precio)

print("Productos en el carrito: ", len(carrito))
print("Precios de los productos en el carrito: ", sum(carrito))
