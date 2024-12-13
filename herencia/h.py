# h. Registro de dispositivos: Crea una clase Dispositivo con atributos protegidos. Implementa subclases como Laptop y Tablet que amplíen su funcionalidad.

class Dispositivo:
    def __init__(self, marca, tamaño, capacidad):
        self.__marca = marca
        self.__tamaño = tamaño
        self.__capacidad = capacidad
    
    def get_marca(self):
        return self.__marca
    def set_marca(self, marca):
        self.__marca = marca

    def get_tamaño(self):
        return self.__tamaño
    def set_tamaño(self, tamaño):
        self.__tamaño = tamaño

    def get_capacidad(self):
        return self.__capacidad
    def set_capacidad(self, capacidad):
        self.__capacidad = capacidad
    

class Laptop(Dispositivo):
    def __init__(self, modelo, tamaño, capacidad, tiene_stylus):
        super().__init__(modelo, tamaño, capacidad)
        self._tiene_stylus = tiene_stylus

    def mostrar_atributos(self):
        return f"Laptop - Marca: {self.get_marca()} - Tamaño: {self.get_tamaño()} - Capacidad: {self.get_capacidad()} - Stylus: { 'Incluido' if self._tiene_stylus else 'No inbcluido'}"
    
    def tiene_stylus(self):
        return self._tiene_stylus

class Tablet(Dispositivo):
    def __init__(self, modelo, tamaño,  capacidad, tiene_gpu):
        super().__init__(modelo, tamaño, capacidad)
        self._tiene_gpu = tiene_gpu

    def mostrar_atributos(self):
        return f"Tablet - Marca: {self.get_marca()} - Tamaño: {self.get_tamaño()} - Capacidad: {self.get_capacidad()} GPU: {'Invluido ' if self._tiene_gpu else 'No incluido'}"
    
    def tiene_gpu(self):
        return self._tiene_gpu 
    
laptop = Laptop("Dell", "15 pulgadas", "1TB", True)
print(laptop.mostrar_atributos())

tablet = Tablet("Samsung", "10 pulgadas", "128GB", True)
print(tablet.mostrar_atributos())