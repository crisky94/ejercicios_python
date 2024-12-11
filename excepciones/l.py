# l. Excepción personalizada para formato de nombre
# Define una excepción personalizada llamada FormatoNombreError. Crea una función verificar_nombre(nombre) que lance esta excepción si el nombre no comienza con una letra mayúscula o contiene números.

import re

class FormatoNombreError(Exception):
    pass

def verificar_nombre(nombre):
    if not nombre[0].isupper():
        raise FormatoNombreError('El nombre debe comenzar con una letra mayúscula')
    
    if re.search(r'\d', nombre):
        raise FormatoNombreError('El nombre no puede conetener números')
    
    return nombre

try:
    nombre = input('Escribe tu nombre: ')
    verificar_nombre(nombre)
    print(f'¡Beunas {nombre}!')
except FormatoNombreError as e:
    print(f'FormatoNombreError: {e}')