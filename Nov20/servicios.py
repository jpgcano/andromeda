inventario = [
    
{
    "nombre": "arroz",
    "precio": 3000.0,
    "cantidad": 3
},
{
    "nombre": "panela",
    "precio": 4000.0,
    "cantidad": 2
},
{
    "nombre": "frijoles",
    "precio": 7000.0,
    "cantidad": 2
},
{
    "nombre": "lentejas",
    "precio": 4000.0,
    "cantidad": 3
}

]

# Documentar cada función con docstring(Qué hace, parámetros, retorno)
def agregar_producto(inventacrio, nombre, precio, cantidad):
    print()
    

def mostrar_inventario(inventario):
    print()


def buscar_producto(inventario, nombre):
    encontrado = False
    flag = True
    while flag:
        ### pedimos ingresar el nombre del producto.
        nombre = input("Por favor ingrese el nombre del producto: ").lower() 
            ### recorremos el dicionario para validar si el producto existe.
        for producto in inventario:
            if nombre in producto["nombre"].lower():
                print(producto)### imprimimos producto.
                encontrado =True
        if not encontrado:
            print("El producto no ha sido encontrado")

def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    print()


def eliminar_producto(inventario, nombre):
    print()


def calcular_estadisticas(inventario):
    print()