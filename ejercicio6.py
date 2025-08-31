import random
import time

def menu_luces():
    while True:
        print("\n=== CONTROL DE LUCES AUTOMÁTICO ===")
        print("1. Iniciar simulación")
        print("2. Reiniciar simulación")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            for _ in range(5):
                noche = random.choice([True, False])
                movimiento = random.choice([True, False])
                if noche and movimiento:
                    print("LUCES ENCENDIDAS")
                else:
                    print("LUCES APAGADAS")
                time.sleep(2)
        elif opcion == "2":
            continue
        elif opcion == "3":
            print("Saliendo del sistema de luces")
            break
        else:
            print("Opción inválida.")


menu_luces()
