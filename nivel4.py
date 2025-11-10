# 19.Lista de frutas.
frutas = ["uva","kiwi","pera", "fresas", "manzana","mandarina","banano","mango"]
for fruta in frutas: 
    print("Me gusta la/el",fruta)

# 20.Agregar y eliminar elementos de la lista.
frutas = ["uva","kiwi","pera", "fresas", "manzana","mandarina","banano","mango"]
for fruta in frutas: 
    print("Me gusta la/el",fruta)
Lista_de_frutas= input("Ingrese una fruta: ")
frutas.append(Lista_de_frutas)
print("La lista de frutas es: ",frutas)
frutas.remove(input("Ingrese la fruta que quiere eliminar: "))
print("La lista de frutas actual, es: ",frutas)
#usamos la propiedad .remove para eliminar elementos dentro de las listas.

# 21.Buscar un elemento en la lista.

frutas = ["uva","kiwi","pera", "fresas", "manzana","mandarina","banano","mango"]
for fruta in frutas: 
    print("Me gusta la/el",fruta)

Lista_de_frutas= input("Ingrese una fruta: ")
frutas.append(Lista_de_frutas)
print("La lista de frutas es: ",frutas)
frutas.remove(input("Ingrese la fruta que quiere eliminar: "))
print("La lista de frutas actual, es: ",frutas)

#.append nos ayuda a encontrar un elemento dentro de una lista.



# 22.Lista de números y promedio.
lista_numeros_promedio = [1, 4, 5, 6, 3, 9, 8, 7, 2, 10]
promedio = sum(lista_numeros_promedio) / len(lista_numeros_promedio)
print("La lista de números es: ", lista_numeros_promedio)
print("El promedio de los números es: ", promedio)


# 23.Números pares: guardar solo los pares.

lista_numeros=[]
for i in range (0,100):
    if i % 2 ==0:
        lista_numeros.append(i)
print("La lista de numeros pares son: ", lista_numeros)


#24.Eliminar duplicados.
frutas = ["uva","kiwi","pera", "fresas", "manzana", "kiwi","mandarina","banano","mango","fresa", "uva", "kiwi"]
frutas_sin_duplicados = []

for n in frutas:
    if n not in frutas_sin_duplicados:
        frutas_sin_duplicados.append(n)

print("La lista de frutas sin duplicados es: ", frutas_sin_duplicados)