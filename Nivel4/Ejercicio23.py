# Ejercicio 23
pares = []

while True:
    numero = int(input("Por favor ingresa un número (ingresa 0 para finalizar): "))

    if numero == 0:
        break 
    
    if numero % 2 == 0:
        pares.append(numero)
        print(f"El número {numero} es par y ha sido agregado a la lista.")
    
    else:
        print(f"El número {numero} es impar y no será agregado a la lista.")

print("Lista final de números pares ingresados:", pares)
