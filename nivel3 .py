"""#-------- primer punto--------
#utilice el bucle for para que al imprimer los numeros del 1 al 11
#al principio pobre del 0 al 9 pero no era lo que me pedian 
#la i es una variable que va a tomar cada valor del rango y la puedo indicar en el print para señalar lo que quiero que salga en la terminal 
for i in range (1, 11): 
    print("este es el numero:", i)
"""
"""#--------segundo punto--------
# use n como variable para pedir un numero al usuario
#y en el rango le sume 1 para que llegue hasta el numero ingresado por el usuario
n = int(input("ingrese un numero: "))
for i in range ( 1+n):
     print("este es el numero:", i)
"""
"""#--------tercer punto--------
#utilice n como variable para pedir un numero al usuario
#y luego utilice un bucle for para multiplicar ese numero por los numeros del 0 al 10
n = int(input("ingrese un numero para multiplicar: "))

for i in range  (0, 11):
    multiplicacion = n * i
    print("este es el numero: ", n, "x", i, "=", multiplicacion)
    
"""
"""#--------cuarto punto-------- 
i= 10
while i >= 0:
    print(i)
    i -= 1
"""