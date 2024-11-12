# c. Unir elementos de dos listas sin duplicados
# Crea una lista que contenga todos los elementos de dos listas diferentes, eliminando cualquier duplicado en el proceso.
lista1 = ['a', 'b', 'c']
lista2 = ['c', 'd', 'e']


listas = []
listas_set = set()

for item in lista1 + lista2:
    if item not in listas_set:
        listas.append(item)
        listas_set.add(item)

print(listas)

# Salida esperada: ['a', 'b', 'c', 'd', 'e']