#------ primer punto--------
"""
#utilice un bucle for para recorrer cada elemento de la lista e imprimir un mensaje que indique que me gusta esa fruta
lista = ["manzana", "banana", "cereza", "durazno", "uva"]
for fruta in lista:
    print("me gusta la:", fruta)

#--------segundo punto--------

#primero utilice la variable frutas para crear una lista de frutas 
#luego pido al usuario que agregue una fruta a la lista con el metodo append
#y despues le pido al usuario que elimine una fruta de la lista con el metodo remove
frutas = ["manzana", "uva", "piña", "mango", "fresa"]
fruta1 = input("agregue una fruta: ")
frutas.append(fruta1)
print(frutas)
fruta2 = input("elimina una fruta de la lista: ")
frutas.remove(fruta2)
print(frutas)

#--------tercer punto--------

#utilice la variable frutas para crear una lista de frutas
#luego pido al usuario que ingrese el nombre de una fruta para buscar su indice en la lista
#si la fruta esta en la lista imprime que la fruta se encuentra en la lista
#si no esta en la lista imprime que la fruta no se encuentra en la lista
frutas = ["manzana", "banana", "cereza", "pera", "uva"]
print("lista original:", frutas)
buscar = input("ingrese el nombre de una fruta para buscarla: ")
if buscar in frutas:
    print(f"La '{buscar}' se encuentra en la lista")
else:
    print(f"La '{buscar}' no se encuentra en la lista")

#--------cuarto punto--------
#en si utilice laformula para sacar el promedio de la lista 
#suma, cantidad, promedio estas variables las utilice para sacar el promedio
numeros = [1,2,3,4,5,6,7,8,9,10]
print("lista original:", numeros)
suma = sum(numeros)
cantidad = len(numeros)
promedio = suma / len(numeros)

print (" el promedio de la lista es:", promedio)

#--------quinto punto-------- 
#uyilice dos variables una para la lista original y otra para agregar los numeros pares
# el for lo utilice para recorrer cada numero de la lista original y con el if verificar si el numero es par
numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
for num in numero:
    if num % 2 == 0:
        pares.append(num)
print("números en la lista:", numero)
print("números pares en la lista:", pares)
"""
#-------sexto punto--------
#utilice set para eliminar los numeros duplicados de la lista
#luego converti el set de nuevo a una lista para mostrar el resultado final
numeros =  [2, 4, 6, 2, 8, 4 , 6,10] 
sinDuplicados = list(set(numeros))
print("Lista original:", numeros)
print("Lista sin duplicados:", sinDuplicados)

