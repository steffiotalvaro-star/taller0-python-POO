def menu_reservas():
    capacidad = 5
    reservas = 0

    while True:
        print("\n=== SISTEMA DE RESERVAS ===")
        print("1. Reservar asiento")
        print("2. Reiniciar reservas")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            if reservas < capacidad:
                reservas += 1
                print(f"Asiento reservado. Quedan {capacidad - reservas} asientos disponibles.")
            else:
                print("No hay asientos disponibles.")
        elif opcion == "2":
            reservas = 0
            print("Se reiniciaron las reservas.")
        elif opcion == "3":
            print("Saliendo del sistema de reservas...")
            break
        else:
            print("Opción incorrecta.")


menu_reservas()
