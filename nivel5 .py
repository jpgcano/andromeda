
#-------punto uno--------

nota1= float(input("ingresa la primera nota: "))
nota2= float(input("ingresa la segunda nota: "))
nota3= float(input("ingresa la tercera nota: "))

promedio = (float(nota1) + float(nota2) + float(nota3)) / 3

if promedio >=3.5:
    print("Aprobo con un promedio de: ", promedio)
else:
    print("Reprobo con un promedio de: ", promedio)

#------punto dos--------

carroDecompras = []
cantidad_agregar= int(input("cuantos productos quieres agregar?:"))
for i in range(cantidad_agregar):
    producto = input("agrega un producto en el carrito: ")
    carroDecompras.append(producto)
    
print ("carrito actual" , carroDecompras)

cantidad_eliminar = int(input("cuantos productos quieres eliminar"))
for i in range(cantidad_eliminar):
    eliminar = input("ingresa el producto que quieres eliminar: ")
if eliminar in carroDecompras: 
    carroDecompras.remove(eliminar)
else: 
    print ("ese producto no esta en el carrito.")

#------punto tres------- 

saldo = 100.000 
print ("1. consultar saldo")
print ("2. depositar saldo")
print ("3. retirar dinero")

opcion = int(input("elige una opcion (1, 2 o 3): "))
if opcion == 1:
  print ("tu saldo actual es:", saldo )
elif opcion == 2: 
        deposito = float(input("ingresa la cantidad a depositar"))
        saldo += deposito 
        print("depositar exitoso tu saldo es" , saldo  )
elif opcion == 3: 
        retiro = float(input("ingresa la cantidad para retirar: "))
        if retiro <= saldo:
            saldo -= retiro 
            print("retiro exitoso, tu nuevo saldo es: ")
        else:
            print("fondos insuficientes.")
else: 
    print("opcion no valida, intentalo de nuevo.")
#-------- punto cuatro ---------

estudiantes = []
while  True: 
    print (" 1. agregar estudiante")
    print ("2. eliminar estudiante")
    print ("3. mostrar lista de estudiantes")
    print ("4. salir")
    opcion = input("elige una opcion (1-4): ")
    if opcion == "1":
        nombre = input("ingresa el nombre del estudiante: ")
        estudiantes.appened(nombre) 
    elif opcion == "2":
        nombre = input("ingresa el nombre del estudiante a eliminar:")
        if nombre in estudiantes : 
            estudiantes.remove(nombre)
            print ("estudiante eliminado correctamente")
        else:
            print (" ese estudiante no esta en la lista")
    elif opcion =="3": 
        if estudiantes:
            print ("lista de estudiantes:")
            for i, estudiantes in enumerate (estudiantes, start=1):
                print(i,"-", estudiantes)
        else:
            print ("la lista esta vacia")
    elif opcion =="4":
        print ("saliendo del sistema")
        break 
    else:
        print ("opcion no valida. intenta de nuevo.")
#--------punto cinco ---------


