class Producto:
    def __init__(self):
        self.productos={}
        
    def Agregar(self):
            dic ={}
            nombre = input("Ingresa nombre del producto:  ")
            precio = float(input("-ingrese valor del producto:  "))
            cantidad = int(input("Ingrese la cantidad de productos:  "))
            dic["precio"]=precio
            dic["cantidad"]=cantidad
            self.productos[nombre]=(dic)

    def Mostrar(self):
        for nombre, info in self.productos.items():
            print(f"{nombre}: Precio :{info['precio']}; Cantidad :{info['cantidad']}")
        return
    def Estadistica(self):
        menu =  int(input("""
                [1] Valor total del inventario
                [2] Cantidad todal de productos 
                """))
        if menu ==1:
            total = 0
            for producto ,items in self.productos.items():
                total = (items['cantidad']*items['precio'])
                print(f"{producto}:  /n  Precio :{items['precio']}\n  Cantidad :{items['cantidad']}") 
        return
def Menu():
        return """ 
            1- Agregar  Producto
            2- Mostrar  Inventario
            3- Calcular Estadisticas
            4- Salir
            """

def ValidarEntradaMenu():
        inventario = Producto()
        bandera=False
        while(bandera!=True):
            print(Menu())
            try:
                seleccion = int(input("Ingrese el numero de la opción del menú: "))
                if (seleccion ==1):
                    print("haz seleccionado la opción de Agregar producto")
                    inventario.Agregar()
                elif (seleccion ==2):
                    print("haz seleccionado la opción de Mostrar inventario")
                    inventario.Mostrar()
                elif(seleccion ==3):
                    print("haz seleccionado la opción de Calcular estadisticas")
                elif(seleccion ==4):
                    print("haz seleccionado la opción de Salir")
                    bandera = True
                else:
                    print("Opción no valida vuelve a ingresar la opción")
            except:
                print("Error vuelve a ingresar el la opción")



print("")
ValidarEntradaMenu()