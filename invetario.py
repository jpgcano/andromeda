#aca hice unas 4 variables para especificar el nombre, valor, cantidad y costo total del producto
nombre =  input("ingrese el nombre del producto: ")
valor = float(input("ingrese el valor del producto: "))
cantidad = int(input("ingrese la cantidad del producto: "))
costo_total = valor * cantidad
#el comando print muestra en pantalla el mensaje que quiero dar en la cnsola y las variables especifican de donde vienen los datos
print ("El producto es: ", nombre)

print("El valor del producto es: ", valor)
print("La cantidad del producto es: ", cantidad)
print("El costo total de los productos es: ", costo_total)