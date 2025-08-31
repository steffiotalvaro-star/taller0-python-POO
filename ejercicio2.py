def menu_fizzbuzz():
    while True:
        print("\n=== JUEGO FIZZBUZZ ===")
        print("1. Ejecutar FizzBuzz")
        print("2. Volver a ejecutar")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            for i in range(1, 101):
                if i % 3 == 0 and i % 5 == 0:
                    print("FizzBuzz")
                elif i % 3 == 0:
                    print("Fizz")
                elif i % 5 == 0:
                    print("Buzz")
                else:
                    print(i)
        elif opcion == "2":
            continue
        elif opcion == "3":
            print("Saliendo del juego...")
            break
        else:
            print("Opción inválida.")


menu_fizzbuzz()
