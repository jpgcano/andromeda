class estudiantes():
    def __init__(self,nombre):
        self.nombre= nombre
        self.materias= {}
    def AgregarMaterias(self,materia):
        if materia not in self.materias:
            self.materias[materia]=[]
        else:
            print(f"la materia '{materia}' ya existe")
    def EliminarMateria(self,materia):
        if materia in self.materias:
            del self.materias[materia]
            print(f"Materia '{materia}' eliminada")
        else:
            print(f"la Materia '{materia}' no existe")
    def RegistrarCalificacion(self, materia, notas):
        if not isinstance(materia, str):
            raise TypeError("El nombre de la materia debe ser texto (str)")
        if materia in self.materias:
            if isinstance(notas,(int,float)):
                self.AgregarMaterias[materia].append(notas)
                print(f"Notas registrada con exito")
            elif isinstance(notas,list):
                self.materias[materia].extend(notas)
                print(f"Notas registrada con exito")
        else:
            print(f"La materia '{materia} no existe'")
    def CalificarNotas(self,materia):
        """
            Manejo de error
        """
        try:
            notas = self.materias[materia]
            if not notas or not all(isinstance(n, (int, float)) for n in notas):
                raise ValueError("datos de notas no valido")
            promedio =sum(notas)/len(notas)
            if (promedio>=3):
                return "Execelente" if promedio==5 else "Aprobado"
            else:
                return "Reprobado"
        except ValueError:
            return "datos de notas no valido"
# === TESTS ===
estudiantes_lista = [
    estudiantes("Juan"),
    estudiantes("Ana"),
    estudiantes("Pedro")
]

print("=== TEST 1: Agregar materias ===")
estudiantes_lista[0].AgregarMaterias("Matemáticas")
estudiantes_lista[1].AgregarMaterias("Historia")
estudiantes_lista[2].AgregarMaterias("Ciencias")

print("\n=== TEST 2: Registrar calificaciones ===")
estudiantes_lista[0].RegistrarCalificacion("Matemáticas", [4.5, 5.0, 3.8])
estudiantes_lista[1].RegistrarCalificacion("Historia", [2.5, 2.8])
estudiantes_lista[2].RegistrarCalificacion("Ciencias", [3.5, 4.0, 4.2])

print("\n=== TEST 3: Calificar materias ===")
for est in estudiantes_lista:
    for materia in est.materias.keys():
        resultado = est.CalificarNotas(materia)
        print(f"{est.nombre} - {materia}: {resultado}")

print("\n=== TEST 4: Eliminar materia ===")
estudiantes_lista[1].EliminarMateria("Historia")
estudiantes_lista[1].EliminarMateria("Historia")  # ya eliminada