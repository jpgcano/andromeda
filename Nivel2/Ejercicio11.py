# Ejercicio 1
calificacion = float(input("Por favor ingresa tu calificación (0.0 - 5.0): ")) 
if calificacion <= 5.0 and calificacion >= 4.0:
    print("Excelente")
elif calificacion < 4.0 and calificacion >= 3.0:
    print("Aprobado")
else:
    print("Reprobado")
    