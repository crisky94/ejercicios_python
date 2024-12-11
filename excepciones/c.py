# c. Comprobación de lista vacía
# Escribe una función obtener_primero(lista) que devuelva el primer elemento de una lista o lance una excepción si la lista está vacía.


# lista = ['Hola Mundo', 'patata']
lista = []

def obtener_primero(lista):
    if len(lista) == 0:
        raise ValueError('La lista estâ vacía.')
    else:
        return lista[0]
    
try:
    print(obtener_primero(lista))
except ValueError as e:
    print(f'Error: {e}')
