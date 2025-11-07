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
print   ("ejercio 1 ")
nombre  = input ("por favor Ingrese su nombre: ")
edad    = int   (input("Por favor ingrese su edadd: "))
print   (f"Hola {nombre}, tienes {edad} años")
print   ("------------------------------")

print   ("ejercio 2 ")
num1    = int   (input("Ingrese el primer número: "))
num2    = int   (input("Ingrese el segundo número: "))
suma    = num1 + num2
print   (f"La suma de {num1} y {num2} es {suma}")
print   ("------------------------------")

print   ("ejercio 3 ")
base    = float (input("Ingrese la base del rectángulo: "))
altura  = float (input("Ingrese la altura del rectángulo: "))
area    = base * altura
print   (f"El area del triangulo es: {area}")
print   ("------------------------------")

print       ("ejercio 4 ")
celsius     = float(input("Ingrese grados celsius"))
Fahrenheit  = (celsius*1.8)+32
print       (f"los grados es fahrenheit es: {Fahrenheit}°F")
print   ("------------------------------")

print       ("ejercio 5 ")
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