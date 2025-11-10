# Ejericio 17
import random

numero_aleatorio = random.randint(1, 10)

print("Adivina el número random entre 1 y 10")

intento = None
intentos = 0

while intento != numero_aleatorio:
    intento = int(input("Ingresa tu número: "))
    intentos += 1

    if intento < numero_aleatorio:
        print("Demasiado bajo, intenta con un número mayor.")
    elif intento > numero_aleatorio:
        print("Demasiado alto, intenta con un número menor.")
    else:
        print("¡Felicidades! Has adivinado el número.")
        print(f"Te ha tomado {intentos} intentos adivinar el número.")
