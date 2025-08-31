import random

def menu_intrusos():
    alarma_activada = False

    while True:
        print("\n=== DETECCIÓN DE INTRUSOS ===")
        print("1. Activar alarma")
        print("2. Desactivar alarma")
        print("3. Salir")

        opcion = input("Escoge una opción: ")

        if opcion == "1":
            alarma_activada = True
            for _ in range(5):
                sensores = [random.choice([True, False]) for _ in range(3)]
                noche = random.choice([True, False])
                print(f"Sensores: {sensores}, Noche: {noche}")
                if sensores.count(True) >= 2 and noche and alarma_activada:
                    print("ALARMA ACTIVADA")
                else:
                    print("Sistema seguro.")
        elif opcion == "2":
            alarma_activada = False
            print("La alarma está desactivada.")
        elif opcion == "3":
            print("Saliendo del sistema de intrusos")
            break
        else:
            print("Opción inválida.")


menu_intrusos()
