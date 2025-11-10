# Ejercicioo 12
numero1 = int(input("Por favor ingresa un número 1: "))
numero2 = int(input("Por favor ingresa un número 2: "))
numero3 = int(input("Por favor ingresa un número 3: "))
if numero1 >= numero2 and numero1 >= numero3:
    print(f"El número mayor es: {numero1} que es el número 1")
elif numero2 >= numero1 and numero2 >= numero3:
    print(f"El número mayor es: {numero2} que es el número 2")
else:
    print(f"El número mayor es: {numero3} que es el número 3")
