def menu_calculadora():
    while True:
        print("\n=== CALCULADORA SIMPLE ===")
        print("1. Realizar un cálculo")
        print("2. Reiniciar calculadora")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            num1 = float(input("Digite el primer número: "))
            num2 = float(input("Digite el segundo número: "))
            operacion = input("Elige operación (+, -, *, /): ")

            if operacion == "+":
                print("Resultado:", num1 + num2)
            elif operacion == "-":
                print("Resultado:", num1 - num2)
            elif operacion == "*":
                print("Resultado:", num1 * num2)
            elif operacion == "/":
                if num2 != 0:
                    print("Resultado:", num1 / num2)
                else:
                    print("Error: división entre 0.")
            else:
                print("Operación inválida.")
        elif opcion == "2":
            continue
        elif opcion == "3":
            print("Saliendo de la calculadora...")
            break
        else:
            print("Opción inválida.")


menu_calculadora()
