# Solicitar datos al usuario
nombre = str(input("Por favor ingresa el nombre del producto: "))

# Solicitar precio
while True:
    precio_und = float(input("Por favor ingresa el precio: "))
    precio = precio_und
    print(f"${precio}")
    
    if precio > 0:
        break
    else:
        print("El precio es inválido. Por favor ingrese el dato de nuevo.")
    
# Solicitar cantidad
while True:
    cantidad = int(input("Por favor ingrese la cantidad: "))

    if cantidad > 0:
        break
    else:
        print("La cantidad ingresada es inválida. Por favor ingresa el dato de nuevo.")

# Operación matemática
costo_total = precio*cantidad

# Resultado para la consola
print(f"El nombre del producto es {nombre}, el precio es ${precio} por unidad, la cantidad es {cantidad} y el costo total es ${costo_total}.")


'''El programa solicita varios datos al usuario (Producto, precio, cantidad). Esto lo realiza por medio de varias funciones, y dividido en varios 
pasos, el primer paso consta de solicitar el nombre del producto, el segundo paso se le solicita el precio, el tercer paso la cantidad de dicho 
producto, el cuarto paso se realiza la operación matemática y por último se muestra en consola el resultado, dando así como finalizado el proceso'''