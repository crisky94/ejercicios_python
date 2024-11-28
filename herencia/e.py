#### e. **Inventario de vehículos:** Crea una clase base `Vehiculo` con métodos para obtener detalles y atributos protegidos. Define subclases como `Auto` y `Motocicleta`.
class Vehiculo:
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
    def get_marca(self):
        return self._marca
    def get_modelo(self):
        return self._modelo
    def detalles(self):
        return f'Marca: {self._marca}, Modelo: {self._modelo}'

class Auto(Vehiculo):
    def __init__(self, marca, modelo, numero_puertas):
        super().__init__(marca, modelo)
        self._numero_puertas = numero_puertas
    
    def get_numero_puertas(self):
        return self._numero_puertas
    
    def detalles(self):
        return f'{super().detalles()}, Numero de puertas: {self._numero_puertas}'

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, tipo_motor):
        super().__init__(marca, modelo)
        self._tipo_motor = tipo_motor
    def get_tipo_motor(self):
        return self._tipo_motor
    
    def detalles(self):
        return f'{super().detalles()}, Tipo de motor: {self._tipo_motor}'


auto = Auto('Citroen', 'c5', 5)
print(auto.detalles())

moto = Motocicleta('Yamaha', 'YZF-R3', 'Motor bicilíndrico')
print(moto.detalles())
        