

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

""" 
def RegistrarPacientes ():
    historial =[]
    dianostico=[]
    informacionInicial=()
    while True:
        print ("--REGISTRO DE PACIENTES--")
        print ("1. Ingresa tu numero de CC: ")
        print ("2. Ingresa tu nombre completo: ")
        print ("3. Ingresa tu edad: ")
        print ("4. Ingresa tu genero: ")
        print ("5. Salir. ")
        
        opcion = input("inicia tu registro del (1-4): ")
        
        if opcion == "1":
            CC = input("Ingrese tu numero de identificacion ciudadana: ")
            print ("Su numero de identificacion es: {CC} ")
        
        elif opcion == "2": 
            nombre = input("Ingrese su nombre completo (nombres y apellidos ): ")
            print("Su nombre completo es {nombre}")
        elif opcion == "3":
            edad = input("Ingresa tu edad: ")
            print ("Tu edad es {edad} ")
        elif opcion == 4:
            genero = input("Cual es tu genero (Masculino , Femenino, Otros ): ")
            print ("su genero es {genero}")
        elif opcion == "5": 
            print ("--SALIENDO DEL REGISTRO--")
            break

        return
"""

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
def ActualizarPacientes(): ### Primero ahcer el buscar pacientes
    return
def ElininarPacientes():
    return
def Reporte():
    return

#RegistrarPacientes()
BuscarPacientes()