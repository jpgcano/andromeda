
# Se le solicita al usuario que ingrese el nombre de un producto.
nombre = str(input("Ingrese el nombre del producto: "))

# Se le solicita al usuario que ingrese el precio de el producto.
while True:
    precio_unitario = float(input("Ingrese el precio del producto:$ "))
    precio = precio_unitario
    print(precio)
    if precio > 0:
        break
    else:
        print("El precio no puede ser negativo o cero. Intente de nuevo.")

# Se le solicita al usuario que ingrese la cantidad de el producto.
while True:
    cantidad = int(input("Ingrese la cantidad del producto: "))
    if cantidad > 0:
        break
    else:
        print("La cantidad no puede ser negativa o cero. Intente de nuevo.")

# Se calcula el costo total del producto.
costo_total = precio*cantidad
print("El costo total es:$ ", costo_total)

print("proucto: ",nombre, "precio unitario:$ ",precio, "cantidad: ",cantidad, "total:$ ",costo_total)

"""
El programa completo permite que un usuario interactue con el sistema para facilitar
el ingreso de productos, calculando asi el costo total dependiendo del precio
ingresado y la cantidad de productos.

"""