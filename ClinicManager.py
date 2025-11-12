

pacientes ={"id": 1,
  "nombre": "Carlos Pérez",
  "edad": 45,
  "genero": "Masculino",
  "diagnostico": "Hipertensión",
  "historial": ["Consulta general", "Control presión arterial"]
  }
def RegistrarPacientes():
    historial =[]
    dianostico=[]
    informacionInicial=()
    return
def BuscarPacientes():
    id = int(input("Ingresa el número de documento del paciente: "))
    valor = input("Por favor ingrese el nombre del paciente: ")
    for dicc in pacientes:
        if dicc["nombre"] == valor:
            return dicc
        elif dicc["id"] == id:
            return dicc
def ActualizarPAcientes(): ### Primero ahcer el buscar pacientes
    return
def ElininarPacientes():
    return
def Reporte():
    return

print(BuscarPacientes())