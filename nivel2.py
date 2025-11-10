#7.
#Le pedimos al usuario que ingere su edad para conocer si es mayor de edad o no.
edad = input("Ingresa tu edad:")
edad = int(edad)
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")


#8.
#Le pedimos al usuario que ingrese un número para conocer si este es positivo negativo o cero.
numero = int(input("Ingresa un numero: "))

if numero > 0:
    print("El numero es positivo")
elif numero == 0:
    print("El numero es cero")
else:
    print("El numero es negativo")


#9.
#Realizamos esta formula para conocer que número es par o impar.
numero_par_impar = int(input("Ingresa un número para saber si es par o impar: "))
if numero_par_impar % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")

#10.
# Le pedimos al usario que ingrese un número dos números.
number1=float(input("Ingresa el primer número: "))
number2=float(input("Ingresa el segundo número: "))

#Le pedimos al usuario que ingrese que operacion básica quiere realizar (+, -, *, /)
operacion= input("Ingresa la operación (+, -, *, /): ")
if operacion == "+":
    resultado= number1 + number2
    print("El resultado de la suma es:", resultado)
elif operacion == "-":
    resultado= number1 - number2
    print("El resultado de la resta es:", resultado)
elif operacion == "*":
    resultado= number1 * number2
    print("El resultado de la multiplicación es:", resultado)
elif operacion == "/":
    if number2 != 0:
        resultado= number1 / number2
        print("El resultado de la división es:", resultado)
    else:
        print("Error: No se puede dividir entre cero.")
#Imprimimos el mensaje según la operación realizada.    

#11 Calificador de notas
# Le pedimos al usuario que escriba una calificación para saber si es Excelente, aprobo o reprobó.
nota= float(input("Ingrese una calificación (0 - 5): "))
if nota == 4 and nota <=5:
    print("Excelente")
elif nota >= 3 and nota <=4:
    print("Aprobado")
elif nota >=0 and nota <=3:
    print("Reprobado")

#Imprimimos el mensaje según la calificacion realizada.    


#6.Comparador de tres números: mayor y menor.
number1 = int(input("Ingresa un numero: "))
number2 = int(input("Ingresa otro numero: "))
number3 = int(input("Ingresa un tercer numero: "))

if number1 >= number2 and number1 >= number3:
    mayor = number1
    print("El número mayor es:", mayor)
elif number2 >= number1 and number2 >= number3:
    mayor = number2
    print("El número mayor es:", mayor)
else:
    mayor = number3
    print("El número mayor es:", mayor)
if number1 <= number2 and number1 <= number3:
    menor = number1
    print("El número menor es:", menor)
elif number2 <= number1 and number2 <= number3:
    menor = number2