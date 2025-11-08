#--------primer punto-------
#utilice edad como variable para pedir la edad al usuario 
edad = int(input("Ingrese su edad actual: ")) 
#utilice estas condiciones para indicar si ya era mayor de edad o no y dejarle saber que ya esta viejo o es un bebe
if edad >= 18:
    print("ya estas viejo.")
else:
    print("Eres un bebe todavia.")

#--------segundo punto--------- 

#utilice el if para indicar que el numero era positivo 
#utilice el elif para indicar que el numero era negativo
#y el else para indicar que el numero era cero
numero = int(input("Ingrese un numero: "))
if numero >0:
    print("El numero es positivo.")
elif numero <0:
    print("El numero es negativo.")
else:
    print("El numero es cero.")
    
#--------tercer punto--------
 #en estas solo utilices estas condiciones (if y else) para saber si el numero era par o impar
numero = int(input("ingrese un numero: "))
if numero % 2 == 0:
    print("El numero es par.")
else:
    print("El numero es impar.")

#-------cuarto punto-------

#utilice if y elif para indicar cada operacion si era multiplicacion suma... y el else solo fue para division para indicar que la operacion no era valida al dividir 0 
num1 = int(input("Ingrese el primer numero: "))
operacion = input("Ingrese la operacion (+, -, *, /): ")
num2 = int(input("Ingrese el segundo numero: "))
if operacion == "+":
    resultado = num1 + num2
    print("El resultado de la suma es: ", resultado)
elif operacion == "-":
    resultado = num1 - num2
    print("El resultado de la resta es: ", resultado)
elif operacion == "*":
    resultado = num1 * num2
    print("El resultado de la multiplicacion es: ", resultado)
elif operacion == "/":
    if num2 != 0:
        resultado = num1 / num2
        print("El resultado de la division es: ", resultado)
    else:
        print("Error: No se puede dividir por cero.")

#------quinto punto-------- 

#puse el mayor e igual paara que sea esa nota o mayor pero tampoco confunda con otra nota 
#el if lo utilice como la mejor nota el elif como ni tan mal ni tan bien y el else como la peor nota
calificador = float(input("Ingrese su calificacion (0-100): "))
if calificador >= 90:
    print("exelente")
elif calificador >= 50:
    print("aprobado")
else:
    print("reprobado")

#-------sexto punto--------

#utilice if, elif y else para comparar los tres numeros ingresados por el usuario
#y asi saber cual era el mayor de los tres
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))
if num1 >= num2 and num1 >= num3:
    print("El numero mayor es: ", num1)
elif num2 >= num1 and num2 >= num3:
    print("El numero mayor es: ", num2)
elif num3 >= num1 and num3 >= num2:
    print("El numero mayor es: ", num3)
else:
    print ("al menos dos numeros son iguales")