# Ejercicio 10
numero1 = int(input("Por favor ingresa un número: "))
numero2 = int(input("Por favor ingresa otro número: "))
operacion = input("Por favor ingresa la operación a realizar (+, -, *, /): ")

if operacion == "+":
    resultado = numero1 + numero2
    print(f"El resultado de la suma es: {resultado}")
elif operacion == "-":
    resultado =numero1 - numero2
    print(f"El resultado de la resta es: {resultado}")
elif operacion == "*":
    resultado = numero1 * numero2
    print(f"El resultado de la multiplicación es: {resultado}")
elif operacion == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"El resultado de la división es: {resultado}")
    else:
        print("Error: No se puede dividir entre cero.")

        '''esta es una calculadora '''