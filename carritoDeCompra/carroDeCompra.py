def CarroDeCompra():
    producto ={}
    def AgregarProducto(nombre,valor):
        producto[nombre] = valor
        print(f"{nombre} agregado con el valor: {valor}")
    def RemoverProducto(nombre):
        if nombre in producto:
            del producto[nombre]
            print(f"{nombre} eliminado del carrito")
        else:
            print(f"{nombre} no se existe en el carrito")
    return AgregarProducto, RemoverProducto, producto

# Aquí las llamas dentro de la función principal:
AgregarProducto, RemoverProducto, carrito= CarroDeCompra()
AgregarProducto("Camiseta", 35000)
AgregarProducto("Pantalón", 50000)
RemoverProducto("Camiseta")
# Mostrar contenido final
print("Carrito actual:",carrito)