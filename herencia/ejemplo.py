# b. Ejercicio práctico
# Crea una clase Electrodomestico con atributos marca y modelo, y un método encender(). Luego, crea una clase derivada Lavadora que herede de Electrodomestico y añada un atributo capacidad. Implementa un método adicional en Lavadora para iniciar el lavado.

class Electrodomestico:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def encender(self):
        print(f'{self.marca}  {self.modelo} esta encendido.')

class Lavadora(Electrodomestico):
    def __init__(self, marca, modelo, capacidad):
        super().__init__(marca, modelo)
        self.capacidad = capacidad
    def iniciar_lavado(self):
        print(f'{self.marca}  {self.modelo} esta lavando.')

lavadora = Lavadora("samsung", "xp10", "7kg")
lavadora.iniciar_lavado()