# d. Implementa el método __str__ para mostrar información amigable de un objeto Persona.
class Persona:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f'{self.name} {self.age}'

persona = Persona('Kenay', 38)
print(persona)