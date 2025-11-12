class Producto:
    def __init__(self):
        self.producto=[]
    def Agregar(self):
        while True:
            nombre = input("Ingresa nombre del producto")
            precio = float(input("-ingrese valor del producto"))
            cantidad = int(input("Ingrese la cantidad de productos"))
            agregar= input("Continuar agregando SI:[s], NO:[n]")
            if isinstance(nombre(str)) and isinstance(precio(int,float)) and isinstance(cantidad(int)):
                self.producto["nombre"].append(nombre)
                self.producto["precio"].append(precio)
                self.producto["cantidad"].append(cantidad)
            print(f"producto ingresado correctamente {self.producto}")
            if agregar.lower() =="n":
                break
    def Mostrar(self):
        return print(self.producto)




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