# m. Validación de entrada de número
# Define una excepción personalizada llamada NumeroInvalidoError. Escribe una función validar_numero(numero) que valide lo siguiente:

# El número debe ser positivo.
# El número debe ser menor que 100.
# Utiliza múltiples bloques except para manejar errores como ValueError (si el tipo no es un número válido) y NumeroInvalidoError para las validaciones específicas.


class NumeroInvalidoError(Exception):
    pass

def validar_numero(numero):
    if numero < 0:
        raise NumeroInvalidoError('El número no puede ser negativo')
    if numero > 100:
        raise NumeroInvalidoError('El número no puede ser mayor a 100 ')
    

try:
    numero = int(input('Introduce un número entre el 0 y el 100: '))
    validar_numero(numero)
    print(f'El número introducido es: {numero}')
except NumeroInvalidoError as e:
    print(f'NumeroInvalidoError: {e}')
except ValueError as e:
    print({e})