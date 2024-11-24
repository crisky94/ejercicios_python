# c. Crea una clase Persona que valide que la edad sea mayor que cero.

class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = None
        self._edad = edad

    @property
    def edad(self) -> init:
        return self._edad

    @edad.setter
    def edad(self, valor: int) -> None:
        if valor <= 0:
            raise ValueError('La edad debe ser mayor a cero')
        return self.edad = valor
def __Str__(self) -> str:
    return 