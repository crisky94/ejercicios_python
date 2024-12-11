# h. Validación de cadenas
# Crea una función validar_cadena(cadena) que lance una excepción si la cadena está vacía

def validar_cadena(cadena):
    if not cadena:
        raise ValueError('La cadena no puede estar vacía')
    else:
        return cadena
    
try:
    cadena = ''
    validar_cadena(cadena)
    print(f'La cadena es {cadena}')
except ValueError as e:
    print(f'Error: {e}')