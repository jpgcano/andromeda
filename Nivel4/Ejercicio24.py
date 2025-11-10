# Ejercicio 24
numeros = [5,7,2,5,9,1,7]
sin_duplicados = []

for n in numeros:
    if n not in sin_duplicados:
        sin_duplicados.append(n)

print(f"Lista sin duplicados: {sin_duplicados}")
