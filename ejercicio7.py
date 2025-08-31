import random
import time

def menu_ac():
    while True:
        print("\n=== CONTROL DE AIRE ACONDICIONADO ===")
        print("1. Iniciar simulación")
        print("2. Reiniciar simulación")
        print("3. Salir")

        opcion = input("Escoge una opción: ")

        if opcion == "1":
            for _ in range(5):
                temp = random.randint(20, 35)
                humedad = random.randint(30, 80)
                print(f"Temp: {temp}°C, Humedad: {humedad}%")
                if (temp > 28 and humedad > 60) or temp > 30:
                    print("Aire Acondicionado ENCENDIDO ")
                else:
                    print("Aire Acondicionado APAGADO")
                time.sleep(2)
        elif opcion == "2":
            continue
        elif opcion == "3":
            print("Saliendo del sistema")
            break
        else:
            print("Opción inválida.")


menu_ac()
