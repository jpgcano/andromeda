# Ejercicio 14
n = int(input("Por favor ingresa un número para realizar la operación: "))
suma = 0
for i in range(1, n + 1):
    suma = suma + i
    print(f" la suma de los números desde 1 hasta {n} es: {suma}")
