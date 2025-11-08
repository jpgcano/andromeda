#--------primer punto--------
#aca utilice 2 variables para pedir el nombre y la edad al usuario
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
#este print lo utilice para inprimir lo que el usuario ingreso y se vea mas ordenado 
print("Hola " + nombre + ", tienes " + edad + " años.")

#--------segundo punto--------

#con cada variable pio un numero x al usuario y luego con la variable suma hago la suma de los dos numeros
#y utilice int para convertir el valor ingresado por el usuario en un numero entero
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
suma = num1 + num2
#este print lo utilice para inprimir el resultado de la suma
print("la suma de los dos numeros es: ", suma) 

#--------tercer punto--------

#utilice dos variables llamada base y altura para multiplicarlo y despues dividirlo por 2 y asi sacar el area del triangulo
BASE = float(input("Ingrese la base del triangulo: "))
ALTURA = float(input("Ingrese la altura del triangulo: "))
AREA = BASE * ALTURA / 2 
#este print lo utilice para inprimir el area del triangulo
print ("el area del triagulo es : ", AREA)

#--------cuarto punto--------

#utilice una variable para pedir al usuario la temperatura en celcius y luego la converti a fahrenheit con la formula de conversion 
celcius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (celcius * 9/5) + 32
#este print lo utilice para inprimir la temperatura en fahrenheit
print("La temperatura en grados Fahrenheit es: ", fahrenheit)

 #-------quinto punto--------
 
#puse cada tipo de variable con la int puse edad ya que es un numero entero
#con str puse nombre ya que es una cadena de texto
#con float puse valor ya que es un numero decimal  
#con bool puse soy_mayor ya que se puede confirmar con un si o no o en este caso True o False
edad = int(input("Ingrese su edad: "))
print(type(edad))
nombre = str(input("ingresa tu nombre:"))
print(type(nombre))
valor = float(input("ingresa tu valor: "))
print(type(valor))
soy_mayor = bool(input("eres mayor de edad? (true/false): "))  
print(type(soy_mayor))

#--------sexto punto--------

#utilice dos variables una para pedir la edad actual al usuario y otra para calcular la edad en 10 años
#para saber cuantos años tendrá en 10 años le sume 10 a la edad actual
#y utilice int para que quede un numero entero 
edadActual = int(input("Ingrese su edad actual: "))
edadFutura = edadActual + 10
print("En 10 años tendrás: ", edadFutura, " años.")