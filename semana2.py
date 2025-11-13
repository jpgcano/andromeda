inventario = {}
while True: 
    
    print ("---- MENU DE INVENTARIO -----")
    print ("1. agregar producto: ")
    print ("2. mostrar inventario ")
    print ("3. calcular estadisticas:")
    print ("4. salir" )
    opcion = input("elige una opcion del (1 al 3): ")
    
    if opcion == "1":
        producto = input("que producto quiere agregar: ")
        precio = float(input("cual es el precio del producto: "))
        cantidad = int(input("cual es la cantidad del producto: "))
        
        inventario[producto]= {
        "precio" : precio,
        "cantidad" : cantidad,
}
        
        print (f"se agrego {producto} que vale {precio} y la cantidad es {cantidad}  ")   
    elif opcion =="2":
        print (f"producto : {producto} | precio : {precio} | cantidad : {cantidad}") 
    elif opcion == "3":
        if not inventario:
            print ("no hay productos para calcular estadiscticas")
        else:
            totalDelinventario= precio * cantidad
            print ("el valor total del inventario es", totalDelinventario)
            cantidadTotal=cantidad + 0
            print ("la cantidad total de los productos registrados son",cantidadTotal)
                
    elif opcion =="4":
        print ("------ SALIENDO DEL MENU --------")
        break
    


        