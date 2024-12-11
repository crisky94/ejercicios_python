# e. Validación de rango numérico
# Escribe una función verificar_rango(n, min, max) que lance una excepción si un número no está dentro de un rango dado.

def verificar_rango(n, min, max):
    if min > n < max:
        raise ValueError(f'El numero {n} no puede ser menor a {min}, ni mayor a {max}')
    else:
        return n
try:
    n = int(input('Introduce un numero del 5 al 15: '))
    min = 5
    max = 15
    verificar_rango(n, min, max)
    print(f'Has introducido el {n}')
except ValueError as e:
    print(f'Error: {e}')
