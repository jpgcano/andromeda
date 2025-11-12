

pacientes ={}
def RegistrarPacientes ():
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
            
        RegistrarPacientes ()
            
            
            
                           
                                     
                       
    """    
    historial =[]
    dianostico=[]
    informacionInicial=()
    return
def BuscarPacientes():
    return
def ActualizarPAcientes(): ### Primero ahcer el buscar pacientes
    return
def ElininarPacientes():
    return
def Reporte():
    return
    """