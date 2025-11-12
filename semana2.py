inventario = {
producto = []
precio =[]
cantidad =[]
}
while True: 
    print ("1. agregar producto: ")
    print ("2. mostrar inventario ")
    print ("3. calcular estadisticas:")
    print ("4. salir" )
    opcion = input("elige una opcion del (1 al 3): ")
    
    if opcion == "1":
        producto = input("que producto quieres agregar?: ")
        inventario.append (producto)
        print (f"{producto} se agrego al se agrego al inventario")
        precio = float(input("cual es el precio del producto: "))
        inventario.append (precio)
        print (f"{precio}es el nuevo valor del producto ")
        cantidad = int(input("cual es la cantidad del prodcuto: "))
        inventario.append (cantidad)
        print (f"{cantidad} es la cantidad del producto ")
        
    elif opcion =="2":
        print (f"producto: {producto} | precio: {precio} | cantidad:{cantidad}")
        

        
    elif opcion =="4":
        print ("saliendo del menu")
        break
    
        