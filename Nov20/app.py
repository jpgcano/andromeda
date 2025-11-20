
while True:

    print("\n---MENÚ PRINCIPAL---\n")
    print("1.  Agregar.")
    print("2.  Mostrar.")
    print("3.  Buscar.")
    print("4.  Actualizar.")
    print("5.  Eliminar.")
    print("6.  Estadísticas.")
    print("7.  Guardar CSV.")
    print("8.  Cargar CSV.")
    print("9.  Sallir.")

    opcion = int(input("Elige una opción para continuar(1-9): "))

    if opcion == 1:
        print(agregar_producto())

    elif opcion == 2:
        print(mostrar_inventario())

    elif opcion == 3:
        print(buscar_producto())

    elif opcion == 4:
        print(actualizar_producto())

    elif opcion == 5:
        print(eliminar_producto())

    elif opcion == 6:
        print(calcular_estadisticas())

    elif opcion == 7:
        print()

    elif opcion == 8:
        print()

    elif opcion == 9:
        print("Gracias por usasr nuestro servicio.")
        break

    else:
        print("Error: Porfsvor ingrese un número válido.")