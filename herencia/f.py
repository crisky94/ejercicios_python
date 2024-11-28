#### f. **Animales abstractos:** Crea una clase `Animal` que sea abstracta y define subclases como `Perro` y `Pez`, cada una con su propio método `hablar`.
from abc import ABC, abstractmethod

class Animal:
    def __init__(self, nombre):
        self._nombre = nombre

    @abstractmethod
    def hablar(self):
        pass
        
    def __str__(self):
        return f'Animal: {self._nombre}'

class Perro(Animal):
    def hablar(self):
        return f'{self._nombre} dice : ¡Guau! ¡Guau!'

class Pez(Animal):
    def hablar(self):
        return f'{self._nombre} dice: ... (los peces no hacen ruido)'


perro = Perro("Firulais")
pez = Pez("Nemo")

print(perro.hablar())
print(pez.hablar())