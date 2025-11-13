pacientes =[
    {"id": 1,
    "nombre": "Carlos Pérez",
    "edad": 45,
    "genero": "Masculino",
    "diagnostico": "Hipertensión",
    "historial": ["Consulta general", "Control presión arterial"]
    },
    {
        "id": 2,
        "nombre": "Ana Gómez",
        "edad": 32,
        "genero": "Femenino",
        "diagnostico": "Diabetes",
        "historial": ["Chequeo anual", "Control de glucosa"]
    }
]

def MenuBusquedaPacientes():
    print("*******************************")
    print ("Buscar por: ")
    print(f""" 
            1- Nombre parcial
            2- ID
            3- Diagnóstico 
            4- Salir
            """
            )
    return input(" ")

def RegistrarPacientes ():
    historial =[]
    diagnostico=[]
    informacionInicial=[ ]
    while True:
        print ("--REGISTRO DE PACIENTES--")
        print ("1.Inicie registro de paciente ")
        print ("4. mostrar registro y salir")
        dic = {}
        opcion = input("registrate con la opcion 1 ")
        if opcion == "1":
            cc = int(input("Ingrese tu numero de identificacion ciudadana: "))
            dic ["id"] = cc
            print (f"Su numero de identificacion es: {cc} ")
            nombre = input("Ingrese su nombre completo (nombres y apellidos ): ")
            dic ["nombre"] = nombre
            print(f"Su nombre completo es {nombre}")
            edad = int(input("Ingresa tu edad: "))
            dic ["edad"] = edad 
            print (f"Tu edad es {edad} ")
            genero = input("Cual es tu genero: ")
            dic ["genero"] = genero
            print (f"Su genero es {genero}")
            historial = input("historial de usuario: ")
            dic ["historial"] = historial
            print(f"el usuario tiene  {historial}")
            diagnostico=input ("diagnostico del paciente: ")
            dic["diagnostico"] = diagnostico
            print (f"el diagnostico del pacientes{diagnostico}")
            pacientes.append(dic)
        elif opcion == "4":
   
            print (f"Su registro es ", pacientes)
            
            break
        else:
            print ("-------ERROR: Vuelva a registrarse------")    
       
          
RegistrarPacientes()
def BuscarPacientes():
    """ Función para buscar pacientes"""
    flag =True
    while flag:
        """ entramos en un ciclo  para interactuar dentro del menú"""    
        menu = int(MenuBusquedaPacientes()) # llamamos a la función menú
        if menu == 1: ## comparamos el menú con la condición de nombre
            ### pedimos ingresar el nombre del paciente
            nombre = input("Por favor ingrese el nombre del paciente: ").lower() 
            ### recorremos el dicionario para validar si el paciente existe 
            for paciente in pacientes:
                if nombre in paciente["nombre"].lower():
                    print(paciente)### imprimimos paciente
                    break
                else:
                    print("paciente no encontrado") ## imprimimos no encontrado
            break
        elif menu == 2:## validar por IDS
            try: ## evitamos que nos de un error por ingresar texto en vez de numero
                id_buscar = int(input("Ingrese el ID: ")) ## capturamos el ID por teclado
                for paciente in pacientes:  ### recorremos el dicionario para validar si el paciente existe 
                    if id["id"] == id_buscar: ## Comparar ids
                        print(paciente)
                        break
                    else:
                        print("Usuario no existe")
                break
            except ValueError:
                print("El ID debe ser un número.") ## mensaje de error 
        elif menu == 3: ### consultar por diagnostivo
            diag = input("Ingrese el diagnóstico: ").lower()
            for paciente in pacientes: ### recorremos el dicionario para validar si el paciente existe 
                if diag in paciente["diagnostico"].lower():
                    print("Paciente encontrado:",paciente)
                    break
            else:
                print("Paciente no encontrado.")
            break
        elif menu == "4":
            print("Saliendo del buscador de pacientes.") ## saliendo del ciclo 
            flag =False
        else:
            print("Opción no válida. Intente de nuevo.")



def BuscarPacientes():
    """ Función para buscar pacientes"""
    flag =True
    while flag:
        """ entramos en un ciclo  para interactuar dentro del menú"""    
        menu = int(MenuBusquedaPacientes()) # llamamos a la función menú
        if menu == 1: ## comparamos el menú con la condición de nombre
            ### pedimos ingresar el nombre del paciente
            nombre = input("Por favor ingrese el nombre del paciente: ").lower() 
            ### recorremos el dicionario para validar si el paciente existe 
            for paciente in pacientes:
                if nombre in paciente["nombre"].lower():
                    print(paciente)### imprimimos paciente
                    break
                else:
                    print("paciente no encontrado") ## imprimimos no encontrado
            break
        elif menu == 2:## validar por IDS
            try: ## evitamos que nos de un error por ingresar texto en vez de numero
                id_buscar = int(input("Ingrese el ID: ")) ## capturamos el ID por teclado
                for paciente in pacientes:  ### recorremos el dicionario para validar si el paciente existe 
                    if id["id"] == id_buscar: ## Comparar ids
                        print(paciente)
                        break
                    else:
                        print("Usuario no existe")
                break
            except ValueError:
                print("El ID debe ser un número.") ## mensaje de error 
        elif menu == 3: ### consultar por diagnostivo
            diag = input("Ingrese el diagnóstico: ").lower()
            for paciente in pacientes: ### recorremos el dicionario para validar si el paciente existe 
                if diag in paciente["diagnostico"].lower():
                    print("Paciente encontrado:",paciente)
                    break
            else:
                print("Paciente no encontrado.")
            break
        elif menu == "4":
            print("Saliendo del buscador de pacientes.") ## saliendo del ciclo 
            flag =False
        else:
            print("Opción no válida. Intente de nuevo.")




def actualizacion_edad():
    try: ## evitamos que nos de un error por ingresar texto en vez de numero
        id_buscar = int(input("Ingrese el ID del paciente: ")) ## capturamos el ID por teclado
        for paciente in pacientes:  ### recorremos el dicionario para validar si el paciente existe 
            if paciente["id"]  == id_buscar: ## Comparar ids
                nuevaedad = int(input("Ingresa la edad del paciente: "))
                paciente["edad"]= nuevaedad
                break
            else:
                print("Usuario no existe")
    except ValueError:
        print("El ID debe ser un número.") ## mensaje de error 

    return pacientes

print(actualizacion_edad())


def actualizar_diagnostico():
    try: ## evitamos que nos de un error por ingresar texto en vez de numero
        id_buscar = int(input("Ingrese el ID del paciente: "))
        for index, paciente in enumerate(pacientes): 
            if paciente["id"] == id_buscar:
                nuevo_diagnostico = input("Ingresa el nuevo diagnóstico del paciente: ")
                pacientes[index].update({"diagnostico":nuevo_diagnostico})
                print(f"Actualización correcta : {paciente}")
                break
            else:
                print("El ID del paciente no existe.")
    except ValueError:
        print("Error: El ID debe ser un número.")



def actualizacion_historial():
    try: ## evitamos que nos de un error por ingresar texto en vez de numero
        print("ACTUALIZACIÓN DEL PACIENTE")
        id_buscar = int(input("Ingrese el ID: ")) ## capturamos el ID por teclado
        confirmacion = input("Esta seguro que desea agregar este dato al historial del paciente? [si],[no]:  ").lower()
        if confirmacion == "si":
            for index, paciente in enumerate(pacientes):  
                ### recorremos el dicionario para validar si el paciente existe 
                ### Nota: enumerate() nos devuelve un index que nos ayuda a eliminar al usuario.
                if paciente["id"] == id_buscar: ## Comparar ids
                    historial = input("Ingrese la nueva historial:  ")
                    paciente["historial"].append(historial)
                    print("Agregar novedad al historial del paciente: ", paciente)
                """
                    pacientes[index].update({"historial: "})Agregar novedad al historial del paciente: ")
                    print("Agregar novedad al historial del paciente: ")"""
            else:
                    print("No ha sido agregado ninguna novedad")
    except ValueError:
        print("El ID debe ser un número.") ## mensaje de error 

    return
def Reporte():
    return




def EliminarPacientes():
    try: ## evitamos que nos de un error por ingresar texto en vez de numero
        print("ELIMINAR PACIENTES")
        id_buscar = int(input("Ingrese el ID: ")) ## capturamos el ID por teclado
        confirmacion = input("Esta seguro que desea eliminar este paciente? [si],[no]").lower()
        if confirmacion == "si":
            for index, paciente in enumerate(pacientes):  
                ### recorremos el dicionario para validar si el paciente existe 
                ### Nota: enumerate() nos devuelve un index que nos ayuda a eliminar al usuario.
                if paciente["id"] == id_buscar: ## Comparar ids
                    pacientes.pop(index)
                    print("usuario Eliminado")
                    break
                else:
                    print("Usuario no existe")
    except ValueError:
        print("El ID debe ser un número.") ## mensaje de error 

    return
def Reporte():
    return

while True:
    print("--MENÚ PRINCIPAL--")
    print("¡Bienvenido al menú principal!¿Qué quieres hacer el día de hoy?")
    print("1. Registrar pacientes.")
    print("2. Buscar paciente.")
    print("3. Actualizar datos.")
    print("4. Eliminar paciente.")
    print("5. Reportes.")
    print("6. Salir.")

    opcion = int(input("Elija una opcion para continuar(1-6): "))

    if opcion == 1:
        print(MenuBusquedaPacientes())

    elif opcion == 2:
        print(RegistrarPacientes())

    elif opcion == 3:
        print(EliminarPacientes())

    elif opcion == 4:
        print()
        break

    elif opcion == 5:
        print()

    else:
        print("Error: Por favor ingrese un número válido.")




