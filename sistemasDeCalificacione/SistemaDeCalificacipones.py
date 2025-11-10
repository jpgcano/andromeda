""" 
    Nivel 5 — Retos (Integración de todo)
    Objetivo: Aplicar todos los conceptos vistos en problemas más completos.
"""

"""
    Calificación de notas
"""
def CalificarNotas(nota):
    """
        Manejo de error
    """
    try:
        notas = nota
        if not notas or not all(isinstance(n, (int, float)) for n in notas):
            raise ValueError("datos de notas no valido")
        promedio =sum(notas)/len(notas)
        if (promedio>=3):
            return "Execelente" if promedio==5 else "Aprobado"
        else:
            return "Reprobado"
    except ValueError:
        return "datos de notas no valido"


"""
    Ingreso de estudiandes y formato de impresión
"""
def Estudiante(nombre,notas,materia):
    aprueba= CalificarNotas(notas)
    if aprueba is None:
        return f"Error al enviar las notas: {aprueba}"
    return f"""
            Nombre:  {nombre} 
            Materia: {materia}
            Estado:  {aprueba}
            """



"""
    Test de estudiantes
"""
estudiantes = [
    {"nombre": "Alice", "notas": [5, 5, 5], "materia": "Matemáticas"},
    {"nombre": "Bob", "notas": [3.5, 3, 4], "materia": "Ciencias"},
    {"nombre": "Charlie", "notas": [2, 2.5, 1.8], "materia": "Historia"},
    {"nombre": "David", "notas": ["abc", 4, 2], "materia": "Inglés"}
]

for est in estudiantes:
    reporte = Estudiante(est["nombre"], est["notas"], est["materia"])
    print(reporte)

