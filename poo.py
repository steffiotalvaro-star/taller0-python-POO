class Carro:
    def __init__(self,marca, modelo, color):
        self.dato_marca = marca
        self.dato_modelo = modelo
        self.dato_color = color
    
    def set_marca(self, nueva_marca):
        #todos los métodos deben tener parámetros
        self.dato_marca = nueva_marca

    def get_marca(self):
        #todos los métodos get por obligación deben tener retorno
        return self.dato_marca
    
    def imprimir_carro(self):
        print(self.dato_marca, self.dato_modelo, self.dato_color)

    def mover_carro(self, obj_motor):
        #un método que depende de un obj
        obj_motor.arrancar_motor()

    def apagar_carro(self, obj_motor):
        #un método que depende de un obj
        obj_motor.apagar_motor()

class Motor:
    def __init__(self):
        self.estado_motor = None

    def prender_motor(self):
        self.estado_motor = "Prendido"

    def apagar_motor(self):
        self.estado_motor = "Apagado"


##########Zona de código principal##########

obj_carro = Carro("Mazda", "2021", "Negro")
dato_marca = obj_carro.get_marca()
print("Marca Carro:" +dato_marca)
obj_carro.imprimir_carro()

obj_motor = Motor()
obj_carro.mover_carro(obj_motor)
