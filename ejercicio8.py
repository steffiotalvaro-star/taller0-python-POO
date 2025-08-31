import random

def menu_tienda():
    while True:
        print("\n=== CONTROL DE ACCESO A LA TIENDA ===")
        print("1. Iniciar control de acceso")
        print("2. Reiniciar")
        print("3. Salir")

        opcion = input("Escoge una opción: ")

        if opcion == "1":
            for _ in range(5):
                tiene_membresia = random.choice([True, False])
                horario = random.choice([True, False])
                es_empleado = random.choice([True, False])
                print(f"Membresía: {tiene_membresia}, Horario: {horario}, Empleado: {es_empleado}")

                if (tiene_membresia and horario) or es_empleado:
                    print("Acceso PERMITIDO")
                else:
                    print("Acceso DENEGADO")
        elif opcion == "2":
            continue
        elif opcion == "3":
            print("Saliendo del sistema de acceso")
            break
        else:
            print("Opción inválida.")


menu_tienda()
