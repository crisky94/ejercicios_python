# k. Excepción personalizada para rango de edades
# Crea una excepción personalizada llamada EdadInvalidaError. Escribe una función verificar_edad(edad) que utilice esta excepción para indicar si una edad es inválida (negativa o mayor a 120).

class EdadInvalidaError(Exception):
    pass

def verificar_edad(edad):
    if edad < 0 or edad > 120:
        raise EdadInvalidaError(f'La edad: {edad} es inválida, no puede ser negativa, ni igual o superior a 120')
    else:
        return edad

try:
    edad = int(input('Introduce tu edad: '))
    verificar_edad(edad)
    print(f'Tu edad es {edad}')
except EdadInvalidaError as e:
    print(f'EdadInvalidaError: {e}')