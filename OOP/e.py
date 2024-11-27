import random


# e. Implementa una clase Dado que permita tirar un dado de n caras. Luego maneja una serie de 3 dados usando una lista y genera los valores de cada dado iterando la lista.

class Dado:
    def __init__(self, caras=6):
        self.caras = caras
    
    def tirar(self):
        return random.randint(1, self.caras)

dados = [Dado(6), Dado(6), Dado(6)]

resultados = [dado.tirar() for dado in dados]

for i, resultado in enumerate(resultados, start=1):
    print(f'Dado {i}: {resultado}')