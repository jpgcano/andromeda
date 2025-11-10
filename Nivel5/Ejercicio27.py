# Ejercicio 27
saldo = 1000

while True:
    print("CAJERO AUTOMÁTICO")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")

    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        print(f"Tu saldo actual es: ${saldo: }")

    elif opcion == "2":
        deposito = float(input("Ingresa la cantidad a depositar: $"))

        if deposito > 0:
            saldo += deposito
            print(f"Has depositado ${deposito: }. Nuevo saldo: ${saldo: }")

        else:
            print("No puedes depositar una cantidad negativa o cero.")

    elif opcion == "3":
        retiro = float(input("Ingresa la cantidad a retirar: $"))

        if retiro <= 0:
            print("Ingresa una cantidad válida.")
        
        elif retiro > saldo:
            print("No tienes suficiente saldo para retirar esa cantidad.")
        else:
            saldo -= retiro
            print(f"Has retirado ${retiro: }. Nuevo saldo: ${saldo: }")

    elif opcion == "4":
        print("Gracias por usar el cajero. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Intenta nuevamente.")
        