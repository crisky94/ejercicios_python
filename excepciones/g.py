# g. Operación matemática personalizada
# Escribe una función calcular_raiz_cuadrada(n) que maneje valores negativos lanzando una excepción
import math


def calcular_raiz_cuadrada(n):
    
    if n < 0:
        raise ValueError('El número no puede ser negativo')
    resultado = math.sqrt(n)
    return print(f'El resultado es {round(resultado, 1)}')
    
try:
    n = float(input('Introduce un numero para calcular su raiz cuadrada: '))
    calcular_raiz_cuadrada(n)
except ValueError as e:
    print(f'Error: {e}')
