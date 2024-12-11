# j. Validación de divisor múltiple
# Crea una función verificar_multiplo(n, divisor) que lance una excepción si el divisor no es múltiplo de n.

def  verificar_multiplo(n, divisor):
    if n % divisor != 0:
        raise ValueError(f'El l divisor: {divisor} no es múltiplo de {n} ')
    else:
        return n, divisor
    
try: 
    n = float(input('Escribe el número: '))
    divisor = float(input('Escribe el divisor: '))
    verificar_multiplo(n, divisor)
    print(f'El {divisor} es multiple de {n}')
except ValueError as e:
    print(f'Error: {e}')