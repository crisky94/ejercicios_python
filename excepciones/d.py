# d. Conversión segura a entero
# Crea una función convertir_a_entero(valor) que maneje excepciones al convertir cadenas a enteros.
valor = 'patata'

def convertir_a_entero(valor):
    try:
        return int(valor)

    except ValueError:
        raise ValueError(f'El valor "{valor}" no se puede convertir a un entero.')

try:
    convertir_a_entero(valor)
except ValueError as e:
    print(e)