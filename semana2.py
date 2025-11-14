inventario={}
def agregar_productos():
    producto = input("que producto quiere agregar: ")
    precio = float(input("cual es el precio del producto: "))
    cantidad = int(input("cual es la cantidad del producto: "))
    inventario[producto]= {
        "precio" : precio,
        "cantidad" : cantidad,
}
def mostrar_invetario():
    if not inventario:
        print("inventario vacio")
    else:
        print("----- inventario -------")
        for producto, datos in inventario.items():
              print(f"Producto: {producto} | Precio: {datos['precio']} | Cantidad: {datos['cantidad']}")       
def calcular_estadisticas():
    if not inventario:
        print("no hay productos para calcular estadisticas")
    else:
        total_valor = 0
        total_cantidad = 0
        for productos, datos in inventario.items():
            total_valor += datos ["precio"] * datos["cantidad"]
            total_cantidad += datos["cantidad"]
        print("-----ESTADISTICAS------")
        print(f"cantidad total de productos:{total_cantidad}")
        print(f"valor total del invenario: {total_valor}")     
            
         

while True: 
    
    print ("---- MENU DE INVENTARIO -----")
    print ("1. agregar producto: ")
    print ("2. mostrar inventario ")
    print ("3. calcular estadisticas:")
    print ("4. salir" )
    opcion = input("elige una opcion del (1 al 3): ")
    
    if opcion == "1":
        agregar_productos()
       
    elif opcion =="2":
        mostrar_invetario()
    elif opcion == "3":
        calcular_estadisticas()
        
    elif opcion =="4":
        print ("------ SALIENDO DEL MENU --------")
        break
    else:
        print("opcion invalida.intentalo de nuevo")