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
    dianostico=[]
    informacionInicial=()
    while True:
        print ("--REGISTRO DE PACIENTES--")
        print ("1.Inicie registro de paciente ")
        print ("2. mostrar historial")
        print ("3. mostrar registro y salir")
        
        opcion = input("Inicia el registro en la opcion 1 y vea los resultados en la opcion 2: ")
        
        if opcion == "1":
            cc = int(input("Ingrese tu numero de identificacion ciudadana: "))
            pacientes.append (cc)
            historial.append (cc)
            print (f"Su numero de identificacion es: {cc} ")
            nombre = input("Ingrese su nombre completo (nombres y apellidos ): ")
            pacientes.append (nombre)
            historial.append (nombre)
            print(f"Su nombre completo es {nombre}")
            edad = int(input("Ingresa tu edad: "))
            pacientes.append (edad)
            historial.append (edad)
            print (f"Tu edad es {edad} ")
            genero = input("Cual es tu genero: ")
            pacientes.append (genero)
            historial.append (genero)
            print (f"Su genero es {genero}")
        elif opcion=="2":
            print (f"el historial de los pacientes registrados es ", historial)
        
        elif opcion == "3": 
            print (f"Su registro es ", Pacientes)
            
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
def ActualizarPacientes(): ### Primero ahcer el buscar pacientes
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

#RegistrarPacientes()
#BuscarPacientes()
EliminarPacientes()