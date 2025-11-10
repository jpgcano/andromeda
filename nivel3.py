# 13.Contar del 1 al 10.
for i in range (1,11):
    print(i)

   
# 14.Sumatoria del 1 al n.
n=int(input("Ingresa un número n para sumar del 1 al n: "))
suma=0
for i in range (1,n+1):
    suma += i
print("La suma del 1 al", n, "es:", suma)


#15. Tabla de multiplicar.
numero1= int(input("Ingresa un número para multiplicar: "))
numero2= int(input("Ingresa un numero para multiplicar: "))
for i in range (0,11):
    resultado= numero1 * i
    print(f"{numero1} * {i} = ",resultado)

    
#16. Contador regresivo con while.
contador = (int(input("Ingresa un número para el conteo regresivo: ")))
while contador >= 0:
    print(contador)
    contador -= 1



#17.Adivina el número (usar random).

numerosecreto = 66

while True:
    number = int(input("Intente adivinar el numero secreto, ingresa un numero: "))
    if number < numerosecreto:
        print("Tu numero es menor")
    elif number > numerosecreto:
        print("Tu numero es mayor")
    else:
        number == numerosecreto
        print("¡Felicitaciones! haz adivinado el número secreto")
        break

# 18.Sumar hasta que el usuario escriba 0.
suma=0
while True:
    numero = int(input("Ingresa un número para sumar (ingresa 0 para terminar): "))
    if numero == 0:
        break
    suma += numero
print("La suma total es:", suma)
