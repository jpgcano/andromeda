#25.Sistema de calificaciones.


#26.Carrito de compras.
compras= ["Sal","Naranjas","Espinacas","Pan","Aceite","Limones","Bananos","Pimentones","Cerveza"]
carrito_compras= input("Ingrese un artículo del supermercado: ")

compras.append(carrito_compras)
print("Los productos agregados al carrito son: ",compras)
compras.remove(input("Ingrese el articulo que quiere sacar del carrito: "))
print("Los articulos que hay actualmente en tu carrito, son: ", compras)

#usamos  .remove para eliminar elementos dentro de las listas.
#usamos .append para agregar elementos dentro de las listas.


#27.Cajero automático.

saldo=1800
while True :
    print("CAJERO AUTOMÁTICO")
    print("1.Consultar saldo.")
    print("2.Retirar dinero.")
    print("3.Depositar dinero.")
    print("4.Salir.")

    opcion= input("Elige una opción (1-4)")
    if opcion == 1 :
        print ("Tu saldo es: ", saldo)
    elif opcion == "2":
        retiro = float(input("Ingresa la cantidad a retirar:$  "))
        if retiro <= 0:
            print("Ingresa un valor válido")
        elif retiro > saldo:
            print("Fondos insufientes")
        else:
            saldo -= retiro 
            print(f"Haz retirado:$ {retiro} Tu saldo actual es:$ {saldo}")
    elif opcion == 3:
        deposito = float(input("Ingresa la cantidad a depositar:$ "))
        if deposito > 0:
            saldo += deposito
            print (f"Haz depositado{deposito} Tu saldo actual es {saldo}")
        else:
            print("El valor ingresado no puede ser  negativo o cero, vuelve a intentarlo")
    
    elif opcion == 4:
        print("Muchas gracias por usar nuestro cajero, feliz dia.")
        break
    
    else:
        print("Error, vuelve a intentarlo.")


                  

#28.Gestión de estudiantes (mini base de datos).


#29.Calculadora avanzada (usar funciones).
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return 
    return a / b

# Funciones Avanzadas ---

def potencia(base, exponente):
    
    return base ** exponente

def modulo(a, b):
    if b == 0:
        return 
    return a % b

def raiz_cuadrada(a):
    
    if a < 0:
        return "Error: ¡No se puede calcular la raíz cuadrada de un número negativo!"
    return a ** 0.5

# Bucle de la Calculadora 

def iniciar_calculadora():
    
    # Este bucle permite que la calculadora siga funcionando hasta que el usuario decida salir
    while True:
        print("\n--- Selecciona una operación ---")
        print("1. Suma (+)")
        print("2. Resta (-)")
        print("3. Multiplicación (*)")
        print("4. División (/)")
        print("5. Potencia (a^b)")
        print("6. Módulo (Resto)")
        print("7. Raíz Cuadrada (√a)")
        print("8. Salir")

        eleccion = input("Ingresa tu opción (1/2/3/4/5/6/7/8): ")

        if eleccion == "8'":
            print("¡Gracias, Adiós!")
            break 

        # Verificamos si la elección requiere un solo número (Raíz Cuadrada) o dos
        if eleccion in ('1', '2', '3', '4', '5', '6', '7'):
            
            try:
                
                num1 = float(input("Ingresa el primer número: "))
                
                if eleccion == '7':
                    resultado = raiz_cuadrada(num1)
                else:
                    
                    num2 = float(input("Ingresa el segundo número: "))

                    if eleccion == '1':
                        resultado = sumar(num1, num2)
                    elif eleccion == '2':
                        resultado = restar(num1, num2)
                    elif eleccion == '3':
                        resultado = multiplicar(num1, num2)
                    elif eleccion == '4':
                        resultado = dividir(num1, num2)
                    elif eleccion == '5':
                        resultado = potencia(num1, num2)
                    elif eleccion == '6':
                        resultado = modulo(num1, num2)
                        
                print(f"\n El resultado es: {resultado}")

            except ValueError:
                print(" Entrada inválida. Por favor, ingresa solo números.")
                
        else:
            print(" Opción inválida. Por favor, intenta de nuevo.")
agenda_contactos = []


def agregar_contacto(nombre, telefono, email):
    
    nuevo_contacto = {
        "nombre": nombre,
        "telefono": telefono,
        "email": email
    }
    agenda_contactos.append(nuevo_contacto)
    print(f"\n ¡Contacto {nombre} agregado con éxito!")

def mostrar_contactos():
    
    if not agenda_contactos:
        print("\n La agenda está vacía. ¡Agrega tu primer contacto!")
        return

    print("\n Lista de Contactos ")
    

    for i, contacto in enumerate(agenda_contactos):
        
        print(f"ID: {i + 1}")
        print(f"  Nombre: {contacto['nombre']}")
        print(f"  Teléfono: {contacto['telefono']}")
        print(f"  Email: {contacto['email']}")
        print("----------------")

def buscar_contacto(nombre_buscado):
    
    resultados = []
    
    for contacto in agenda_contactos:
        if nombre_buscado.lower() in contacto['nombre'].lower():
            resultados.append(contacto)
            
    if resultados:
        print(f"\n--- Resultados de la búsqueda para '{nombre_buscado}' ---")
        for contacto in resultados:
            print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}")
        print("---------------------------")
    else:
        print(f"\n No se encontraron contactos con el nombre '{nombre_buscado}'.")

print(" Iniciando Agenda")

# Se agregan contactos
agregar_contacto("Maria Camila Vidales", "3054070134", "mariacvidales@gmail.com")
agregar_contacto("Ana Gonzalez", "555-5678", "anacortes1@gmail.com")
agregar_contacto("Luis Orozco", "3013456789", "luisoro@gmail.com")

mostrar_contactos()

buscar_contacto("ana")
buscar_contacto("Pedro")