pacientes = [
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
    },
    {
        "id": 3,
        "nombre": "Luis Martínez",
        "edad": 67,
        "genero": "Masculino",
        "diagnostico": "Artritis",
        "historial": ["Control de dolor", "Fisioterapia"]
    },
    {
        "id": 4,
        "nombre": "María Rodríguez",
        "edad": 58,
        "genero": "Femenino",
        "diagnostico": "Hipotiroidismo",
        "historial": ["Chequeo hormonal", "Control trimestral"]
    },
    {
        "id": 5,
        "nombre": "José Ramírez",
        "edad": 71,
        "genero": "Masculino",
        "diagnostico": "Insuficiencia cardíaca",
        "historial": ["Electrocardiograma", "Control con cardiólogo"]
    },
    {
        "id": 6,
        "nombre": "Laura Herrera",
        "edad": 29,
        "genero": "Femenino",
        "diagnostico": "Asma",
        "historial": ["Evaluación pulmonar", "Ajuste de inhalador"]
    },
    {
        "id": 7,
        "nombre": "Miguel Torres",
        "edad": 63,
        "genero": "Masculino",
        "diagnostico": "Colesterol alto",
        "historial": ["Examen de sangre", "Control nutricional"]
    },
    {
        "id": 8,
        "nombre": "Patricia Mendoza",
        "edad": 54,
        "genero": "Femenino",
        "diagnostico": "Migrañas crónicas",
        "historial": ["Neurología", "Control de medicamentos"]
    },
    {
        "id": 9,
        "nombre": "Andrés López",
        "edad": 23,
        "genero": "Masculino",
        "diagnostico": "Alergias estacionales",
        "historial": ["Pruebas de alergia", "Tratamiento antihistamínico"]
    },
    {
        "id": 10,
        "nombre": "Claudia Silva",
        "edad": 75,
        "genero": "Femenino",
        "diagnostico": "Osteoporosis",
        "historial": ["Densitometría ósea", "Suplementación de calcio"]
    },
    {
        "id": 11,
        "nombre": "Diego Cárdenas",
        "edad": 41,
        "genero": "Masculino",
        "diagnostico": "Gastritis crónica",
        "historial": ["Endoscopia", "Control gastroenterológico"]
    },
    {
        "id": 12,
        "nombre": "Elena Vargas",
        "edad": 68,
        "genero": "Femenino",
        "diagnostico": "Enfermedad pulmonar obstructiva crónica",
        "historial": ["Evaluación respiratoria", "Terapia inhalada"]
    },
    {
    "id": 13,
    "nombre": "Rosa Castillo",
    "edad": 62,
    "genero": "Femenino",
    "diagnostico": "Diabetes",
    "historial": ["Control de glucosa", "Consulta general"]
},
{
    "id": 14,
    "nombre": "Fernando Duarte",
    "edad": 47,
    "genero": "Masculino",
    "diagnostico": "Hipertensión",
    "historial": ["Electrocardiograma", "Control presión arterial"]
},
{
    "id": 15,
    "nombre": "Juliana Patiño",
    "edad": 26,
    "genero": "Femenino",
    "diagnostico": "Asma",
    "historial": ["Evaluación pulmonar", "Ajuste de inhalador"]
},
{
    "id": 16,
    "nombre": "Santiago Ríos",
    "edad": 38,
    "genero": "Masculino",
    "diagnostico": "Migrañas crónicas",
    "historial": ["Neurología", "Control de medicamentos"]
},
{
    "id": 17,
    "nombre": "Gloria Méndez",
    "edad": 73,
    "genero": "Femenino",
    "diagnostico": "Artritis",
    "historial": ["Control de dolor", "Fisioterapia"]
},
{
    "id": 18,
    "nombre": "Eduardo Molina",
    "edad": 52,
    "genero": "Masculino",
    "diagnostico": "Diabetes",
    "historial": ["Chequeo anual", "Control de glucosa"]
},
{
    "id": 19,
    "nombre": "Camila Torres",
    "edad": 34,
    "genero": "Femenino",
    "diagnostico": "Hipertensión",
    "historial": ["Control presión arterial", "Revisión médica"]
},
{
    "id": 20,
    "nombre": "Óscar López",
    "edad": 66,
    "genero": "Masculino",
    "diagnostico": "Artritis",
    "historial": ["Fisioterapia", "Control de dolor"]
},
{
    "id": 21,
    "nombre": "Valentina Sánchez",
    "edad": 22,
    "genero": "Femenino",
    "diagnostico": "Asma",
    "historial": ["Control respiratorio", "Ajuste de medicamentos"]
},
{
    "id": 22,
    "nombre": "Jorge Cáceres",
    "edad": 59,
    "genero": "Masculino",
    "diagnostico": "Migrañas crónicas",
    "historial": ["Consulta neurológica", "Control mensual"]
}

]

def MenuBusquedaPacientes():
    print("*******************************")
    print ("Buscar por: ")
    return print(f""" 
            1- Nombre parcial
            2- ID
            3- Diagnóstico 
            4- Salir
            """
            )
def RegistrarPacientes ():
    historial =[]
    diagnostico=[]
    while True:
        print ("--REGISTRO DE PACIENTES--")
        print ("1.Inicie registro de paciente ")
        print ("2. mostrar registro y salir")
    
        opcion = input("registrate con la opcion: ")
        if opcion == "1":
            dic = {}
            while True:
                try:
                    cc = int(input("Ingrese su numero de identificacion ciudadana: "))
                    dic["id"] = cc
                    if cc > 0 and cc < 1000000000:
                        print (f"Su numero de identificacion es: {cc} ")
                        break
                    else:
                        print("Ingrese una cedula válida, solo números")
                except ValueError:
                    print("Solo es posible agregar números, sin puntos ni comas")
                    
            
            nombre = input("Ingrese su nombre completo (nombres y apellidos ): ")
            dic ["nombre"] = nombre
            print(f"Su nombre completo es {nombre}")

            while True:
                try:
                    edad = int(input("Ingresa tu edad: "))
                    dic ["edad"] = edad
                    if edad > 0 and edad < 120:
                            print (f"Su edad es: {edad} ")
                            break
                    else:
                            print("Ingrese una edad válida, solo números")
                except ValueError:
                    print("Error: Solo es posible agregar números, sin puntos ni comas")

            genero = input("Cual es su genero : ")
            dic ["genero"] = genero
            print (f"Su genero es: {genero}")
            historial = input("historial de usuario: ")
            dic ["historial"] = historial
            print(f"el usuario tiene: {historial}")
            while True:
                diagnostico=input ("diagnostico del paciente: ")
                dic["diagnostico"] = diagnostico
                if diagnostico == "" or diagnostico.isnumeric():
                    print("El diagnostico no debe estar vacio ni puede ser solo numeros.")
                else:
                    break

            print (f"el diagnostico del paciente es: {diagnostico}")
            pacientes.append(dic)
        elif opcion == "2":
            print (f"Su registro es ", dic)
            break
        else:
            print ("-------ERROR: Vuelva a registrarse------")    
 
    

def BuscarPacientes():
    encontrado =False
    """ Función para buscar pacientes"""
    flag =True
    while flag:
        """ entramos en un ciclo  para interactuar dentro del menú"""  
        MenuBusquedaPacientes()  
        menu = int(input()) # llamamos a la función menú
        if menu == 1 and isinstance(menu,int): ## comparamos el menú con la condición de nombre
            ### pedimos ingresar el nombre del paciente
            nombre = input("Por favor ingrese el nombre del paciente: ").lower() 
            ### recorremos el dicionario para validar si el paciente existe 
            for paciente in pacientes:
                if nombre in paciente["nombre"].lower():
                    print(paciente)### imprimimos paciente
                    encontrado =True
            if not encontrado:
                print("paciente no encontrado") ## imprimimos no encontrado
        elif menu == 2 and isinstance(menu,int):## validar por IDS
            try: ## evitamos que nos de un error por ingresar texto en vez de numero
                id_buscar = int(input("Ingrese el ID: ")) ## capturamos el ID por teclado
                for paciente in pacientes:  ### recorremos el dicionario para validar si el paciente existe 
                    if paciente["id"] == id_buscar: ## Comparar ids
                        print(paciente)
                    encontrado =True
                if not encontrado:
                    print("Paciente no encontrado.")
            except ValueError:
                print("El ID debe ser un número.") ## mensaje de error 
        elif menu == 3 and isinstance(menu,int): ### consultar por diagnostivo
            try:
                diag = input("Ingrese el diagnóstico: ").lower()
                for paciente in pacientes: ### recorremos el dicionario para validar si el paciente existe 
                    if diag in paciente["diagnostico"].lower():
                        print(paciente)
                        encontrado =True
                if not encontrado:
                    print("Paciente no encontrado.")
            except ValueError:
                print("diagnóstico no encontrado.") ## mensaje de error
        elif menu == 4 and isinstance(menu,int):
            print("Saliendo del buscador de pacientes.") ## saliendo del ciclo 
            flag =False
        else:
            print("Opción no válida. Intente de nuevo.")
def actualizacion_edad():
    try: ## evitamos que nos de un error por ingresar texto en vez de numero
        id_buscar = int(input("Ingrese el ID del paciente: ")) ## capturamos el ID por teclado
        for paciente in pacientes:  ### recorremos el dicionario para validar si el paciente existe 
            if paciente["id"]  == id_buscar: ## Comparar ids
                print(paciente)
                nuevaedad = int(input("Ingresa la nueva edad del paciente: "))
                
                paciente["edad"]= nuevaedad
                print(paciente)
                encontrado =True
        if not encontrado:
            print("Paciente no encontrado.")
    except ValueError:
        print("El ID debe ser un número.") ## mensaje de error 

def actualizar_diagnostico():
    try: ## evitamos que nos de un error por ingresar texto en vez de numero
        id_buscar = int(input("Ingrese el ID del paciente: "))
        for index, paciente in enumerate(pacientes): 
            if paciente["id"] == id_buscar:
                print(paciente)
                nuevo_diagnostico = input("Ingresa el nuevo diagnóstico del paciente: ")
                pacientes[index].update({"diagnostico":nuevo_diagnostico})
                print(f"Actualización correcta : {paciente}")
                encontrado =True
        if not encontrado:
            print("Paciente no encontrado.")
    except ValueError:
        print("Error: El ID debe ser un número.")
def actualizacion_historial():
    try: ## evitamos que nos de un error por ingresar texto en vez de numero
        print("ACTUALIZACIÓN DEL PACIENTE")
        id_buscar = int(input("Ingrese el ID: ")) ## capturamos el ID por teclado
        for  paciente in pacientes:
                ### recorremos el dicionario para validar si el paciente existe 
                ### Nota: enumerate() nos devuelve  indunex que nos ayuda a eliminar al usuario.
            if paciente["id"] == id_buscar: ## Comparar 
                print(paciente)
                historial = input("Ingrese la nueva historial:  ")
                pacientes.append(historial)
                print("Agregar novedad al historial del paciente: ", paciente)
                """
                    pacientes[index].update({"historial: "})Agregar novedad al historial del paciente: ")
                    print("Agregar novedad al historial del paciente: ")"""
                encontrado =True
        if not encontrado:
            print("Paciente no encontrado.")
    except ValueError:
        print("El ID debe ser un número.") ## mensaje de error 

    return
def Reporte():
    print("**********************************************")
    print("     Bienvenido a la sección de reportes     ")
    menu = int(input(f"""
                Ingrese opción de reporte: 
                [1] Todos los pacientes registrados
                [2] Pacientes mayores de 60 años
                [3] Diagnósticos más frecuentes
                [4] Cantidad total de pacientes
            """))
    if menu ==1 and isinstance(menu, int):
        for paciente in pacientes:
            print("*******************************************")
            print (f"""
        Cedula:         {paciente["id"]},
        nombre:         {paciente["nombre"]},                ,
        edad:           {paciente["edad"]},
        genero:         {paciente["genero"]},   
        diagnostico:    {paciente["diagnostico"]},
        historial:      {paciente["historial"]},
                    """)
    elif  menu ==2 and isinstance(menu, int):
        print("*********************************************")
        for paciente in pacientes:  ### recorremos el dicionario para validar si el paciente existe 
            if paciente["edad"] >= 60: ## Comparar ids
                print("*******************************************")
                print (f"""
                    Cedula:         {paciente["id"]},
                    nombre:         {paciente["nombre"]},                ,
                    edad:           {paciente["edad"]},
                    genero:         {paciente["genero"]},   
                    diagnostico:    {paciente["diagnostico"]},
                    historial:      {paciente["historial"]},
                                """)
    elif menu ==3 and isinstance(menu, int):
        diagnostico = [paciente["diagnostico"] for paciente in pacientes]
        cont ={}
        for diag in diagnostico:
            cont[diag] = cont.get(diag,0)+1
        top = sorted(cont.items(), key=lambda x:x[1], reverse=True)
        for t in top:
            print(f"{t} \n")
    elif menu ==4 and isinstance(menu, int):
        cont = 0
        for paciente in pacientes:
            cont +=1
        print(f"Total de pacientes de la clinica es: ",cont)
        
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

while True:
    print("--MENÚ PRINCIPAL--")
    print("¡Bienvenido al menú principal!¿Qué quieres hacer el día de hoy?")
    print("1. Registrar pacientes.")
    print("2. Buscar paciente.")
    print("3. Actualizar edad.")
    print("4. Actualizar diagnostico.")
    print("5. Actualizar historial.")
    print("6. Eliminar paciente.")
    print("7. Reportes.")
    print("0. Salir.")

    opcion = int(input("Elija una opcion para continuar(1-6): "))

    if opcion == 1:
        print(RegistrarPacientes())
    elif opcion == 2:
        print(BuscarPacientes())
    elif opcion == 3:
        print(actualizacion_edad())
    elif opcion == 4:
        print(actualizar_diagnostico())
    elif opcion == 5:
        print(actualizacion_historial())  
    elif opcion == 5:
        print(EliminarPacientes())
    elif opcion == 6:
        print(EliminarPacientes())
    elif opcion == 7:
        print(Reporte())
    elif opcion == 0:
        print("Gracias por usar nuestro servicio, te esperamos pronto.")
        break
    else:
        print("Error: Por favor ingrese un número válido.")   