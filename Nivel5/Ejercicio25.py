# Ejercicio 25
calificaciones = []

while True:
    nota = float(input("Por favor ingresa una calificación (ingresa -1 para finalizar): "))

    if nota == -1:
        break

    elif nota < 0 or nota > 10:
        print("Calificación inválida. Por favor ingresa una calificación entre 0 y 10.")

    else:
        calificaciones.append(nota)
        print(f"La calificación {nota} ha sido agregada a la lista.")
    
if len(calificaciones) > 0:
    print("Lista final de calificaciones ingresadas:")

    for n in calificaciones:
        estado = "Aprobado" if n >= 6 else "Reprobado"
        print(f"Calificación: {n} - {estado}")

    promedio = sum(calificaciones) / len(calificaciones)
    print(f"El promedio de las calificaciones es: {promedio}")

else:
    print("No se ingresaron calificaciones.")
    