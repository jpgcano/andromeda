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
area    = (base * altura)/2
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
print   ("Ejercicio 11 - nivel 2")
"""Clasificador de notas (Excelente, Aprobado, Reprobado)."""
notas =[3.4,5.5,4.5,5,4,3,2,1,0,3,4,5,1]
for nota in notas:
    if (nota>=3):
        print("Execelente" if nota==5 else "Aprobado")
    else:
        print("Reprobado")


print   ("------------------------------")
print   ("Ejercicio 12 - nivel 2")
"""Comparador de tres números: mayor y menor."""

mayor = 0
menor = 999
for i in range(3):
    num = int(input("Digite un numero"))
    if mayor < num:
        mayor = num
    if menor > num:
        menor = num
print (f"El numenor mayor es: {mayor} y el menor es: {menor}")



print("**********************************************************************************")

"""
    Nivel 3 — Bucles y Repetición
    Objetivo: Dominar for y while, control de iteraciones y sumatorias.
"""

print   ("------------------------------")

print   ("------------------------------")
print   ("Ejercicio 13 - nivel 2")
"""Contar del 1 al 10."""

for i in range(1,10):
    print(i)

print   ("------------------------------")
print   ("Ejercicio 14 - nivel 2")
"""Sumatoria del 1 al n.."""
acumulador =0
n = int(input("Ingrasa el numero a sumar"))
for i in range(n):
    acumulador+=i
print(f"el acumulado es: {acumulador}")

print   ("------------------------------")
print   ("Ejercicio 15 - nivel 2")
"""Tabla de multiplicar."""

tabla = int(input("Ingrese tabla"))
for i in range(1,11):
    print(f"{tabla} * {i} = {tabla*i}")


print   ("------------------------------")
print   ("Ejercicio 16 - nivel 2")
"""Contador regresivo con while.."""
contador = 10
while contador >=0:
    print(contador)
    contador-=1


print   ("------------------------------")
print   ("Ejercicio 17 - nivel 2")
"""Adivina el número (usar random)."""
import random 
seguir =True
secreto = int(random.random()*10)
while seguir == True:
    numero = int(input("ingrese numero: "))
    if(numero ==secreto):
        print("Acertaste, Haz ganado")
        seguir = False
    else:
        print("Fallaste, sigue intentando")

print   ("------------------------------")
print   ("Ejercicio 18 - nivel 2")
"""Sumar hasta que el usuario escriba 0."""
numero =0
acumulador =0
while True:
    n = int(input("Ingrasa el numero a sumar"))
    if n ==0:
        break
    acumulador+=n
print(f"El resultado es : {acumulador}")



"""
    Objetivo: Crear, recorrer, modificar y eliminar elementos en listas.
    Nivel 4 — Listas y Colecciones
"""

print   ("------------------------------")

print   ("------------------------------")
print   ("Ejercicio 19 - nivel 3")
"""Lista de frutas."""
frutas = [
    "manzana","banana", "cereza", "pera",  "uva",
    "mango",  "kiwi",   "sandía",  "melón","naranja",
    "mandarina", "limón","fresa", "arándano", "piña",
    "papaya","maracuyá","guayaba","ciruela", "granada"
]
for fruta in frutas:
    print(fruta)
print   ("------------------------------")
print   ("Ejercicio 20 - nivel 3")
"""Agregar y eliminar frutas."""
frutas = [
    "manzana","banana", "cereza", "pera",  "uva",
    "mango",  "kiwi",   "sandía",  "melón","naranja",
    "mandarina", "limón","fresa", "arándano", "piña",
    "papaya","maracuyá","guayaba","ciruela", "granada"
]
print(frutas)
frutas.remove("mango")
print(frutas)
frutas.append("mango")
print(frutas)


print   ("------------------------------")
print   ("Ejercicio 21 - nivel 3")
"""Lista de números y promedio.."""
frutas = [
    "manzana","banana", "cereza", "pera",  "uva",
    "mango",  "kiwi",   "sandía",  "melón","naranja",
    "mandarina", "limón","fresa", "arándano", "piña",
    "papaya","maracuyá","guayaba","ciruela", "granada"
]
fruta = input("ingrese fruta que deseas buscar")
if fruta in frutas:
    index= frutas.index(fruta)
    print(f"si esta, esta el posición{index} ")