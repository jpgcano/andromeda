"""
    Taller de Consolidación – Ruta Básica de Python
"""

"""
    Nivel 1 – Fundamentos y variables
    Objetivo: Practicar tipos de datos, entrada y salida, concatenación y operaciones básicas.
"""

"""
    Hola usuario: pide al usuario su nombre y edad. Luego imprime un mensaje: "Hola [nombre], tienes [edad] años."
"""
print   ("------------------------------")
print   ("ejercio 1 nivel 1 ")
"""pide al usuario su nombre y edad. Luego imprime un mensaje"""
nombre  = input ("por favor Ingrese su nombre: ")
edad    = int   (input("Por favor ingrese su edadd: "))
print   (f"Hola {nombre}, tienes {edad} años")
print   ("------------------------------")

print   ("ejercio 2 nivel 1 ")
"""Suma de dos números"""
num1    = int   (input("Ingrese el primer número: "))
num2    = int   (input("Ingrese el segundo número: "))
suma    = num1 + num2
print   (f"La suma de {num1} y {num2} es {suma}")
print   ("------------------------------")

print   ("ejercio 3 nivel 1 ")
"""Área del triángulos"""
base    = float (input("Ingrese la base del rectángulo: "))
altura  = float (input("Ingrese la altura del rectángulo: "))
area    = base * altura
print   (f"El area del triangulo es: {area}")
print   ("------------------------------")

print       ("ejercio 4  nivel 1")
"""Conversor de grados Celsius a Fahrenheit"""
celsius     = float(input("Ingrese grados celsius"))
Fahrenheit  = (celsius*1.8)+32
print       (f"los grados es fahrenheit es: {Fahrenheit}°F")
print       ("------------------------------")

print   ("ejercio 5 nivel 1 ")
"""para mostrar el tipo de cada variable"""
print   (type(nombre))
print   (type(edad))
print   (type(num1))
print   (type(num2))
print   (type(suma))
print   (type(base))
print   (type(altura))
print   (type(area))
print   (type(celsius))
print   (type(Fahrenheit))
print   ("------------------------------")

print   ("ejercio 6 ")
"""pide la edad actual y muestra cuántos años tendrá el usuario"""
edad        =  int(input("Ingresa tu edad: "))
edadFutura  = print(f"Dentro de 10 años tengras: {edad+10} ")
print   ("------------------------------")

print("**********************************************************************************")

"""
    Nivel 2 — Condicionales (Decisiones)
    Objetivo: Comprender y aplicar estructuras if, elif, else.
"""

print   ("------------------------------")
""" Definir si eres mayor de edad."""
print   ("Ejercicio 7 - nivel 2")
edad    =   int(input("Ingresa su edad"))
if (edad>=18):
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

print   ("------------------------------")
print   ("Ejercicio 8 - nivel 2")
""" Numero positivo o negativo"""
numero = int(Input("Ingrese nunmero: "))

print   ("------------------------------")
print   ("Ejercicio 9 - nivel 2")
""" Numero para o impar"""
for i in range(100):
    # par ="par" if  i %2==0 else "impar"
    print(i,"par" if  i %2==0 else "impar")
    
print   ("------------------------------")
print   ("------------------------------")
print   ("Ejercicio 10 - nivel 2")
"""Calculadora básica con +, -, *, /."""
resultado =""
num1    = int   (input("Ingrese el primer número: "))
num2    = int   (input("Ingrese el segundo número: "))
operacion =int(input("""Ingresa opeación
                    suma: 1
                    resta: 2
                    multiplicación: 3
                    divición: 4
                """))
if (operacion ==    1):
    resultado    = num1 + num2
elif (operacion ==  2):
    resultado    = num1 - num2
elif (operacion ==  3):
    resultado    = num1 * num2
elif (operacion ==  4):
    resultado    = num1 / num2
else:
    print("operación ingrasada no es valida")
print(f"El resultado es: {resultado}")

print   ("------------------------------")
print   ("------------------------------")
print   ("Ejercicio 10 - nivel 2")
"""Calculadora básica con +, -, *, /."""