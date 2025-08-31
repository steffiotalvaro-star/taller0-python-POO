import time
import random

def menu_invernadero():
    while True:
        print("\n=== CONTROL DE TEMPERATURA EN INVERNADERO ===")
        print("1. Iniciar ")
        print("2. Reiniciar ")
        print("3. Salir ")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            for _ in range(5):
                temp = random.randint(5, 35)
                print(f"Temperatura actual: {temp}°C")
                if temp < 10:
                    print("Estado: Calefactor encendido")
                elif temp <= 25:
                    print("Estado: Normal")
                else:
                    print("Estado: Ventilador encendido")
                time.sleep(2)
        elif opcion == "2":
            continue
        elif opcion == "3":
            print("Saliendo del sistema")
            break
        else:
            print("Opción inválida.")


menu_invernadero()
