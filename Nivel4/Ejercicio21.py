# Ejercicio 21
frutas = ["manzana", "banano", "cereza"]
buscar = input("Por favor ingresa una fruta para buscar en la lista: ")
if buscar.lower() in frutas:
    print(f"La fruta {buscar} esta en la lista.")
else:
    print(f"La fruta {buscar} no esta en la lista.")
