#1
#Se le pide al usuario que ingrese sus datos: nombre y edad.
nombre = input("Por favor, ingresa tu nombre: ")
edad = int(input("Por favor, ingresa tu edad: "))
#Se imprime el mensaje con la información del usuario.
print("hola", nombre, "tienes", edad, "años")

#2.
#Se le pide al usuario que ingrese dos números para realizar una suma.
num1 = float(input("Ingresa el primer número: "))
num2= float(input("Ingresa el segundo número: "))
#realizamos formula para las suma
suma = num1 + num2
#Se imprime la suma de los números.
print(f"La suma de, {num1} y {num2}, es: ",{suma})

#3 
#Se le pide al usuario que ingrese un número de base.
base= float(input("Ingresa la base del triangulo: "))
#Se le pide al usuario que ingrese un número de altura para el triangulo
altura= float(input("Ingresa la altura del triangulo: "))
#Se calcula el área del triángulo
area= (base * altura) / 2
#Se imprime el área del triángulo para conocer su resultado
print("El área del triángulo es: ", area)

#4.
#Se le pide al usuario que ingrese la temperatura en grados Celsius
celsius= float(input("Ingresa la temperatura en grados Celsius: "))
#Realizamos fórmula para calcular la temperatura en grados Farenheit.
fahrenheit= (celsius * 9/5) + 32
print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")


#5.
# #Tipo de dato: usar type() para mostrar el tipo de cada variable.
nombre= "Camila"
print(type(nombre))
edad= 29
print(type(edad))
altura= 1,54
print(type(altura))
peso= 55
print(type(peso))
Pareja= True
print(type(Pareja))


#6.
# #Edad futura: pide la edad actual y muestra cuántos años tendrá el usuario dentro de 10 años.
edad= int(input("Ingresa tu edad actual: "))
edad_futura = edad + 10
print(f"Dentro de 10 años tendrás:", {edad_futura}, "años")
