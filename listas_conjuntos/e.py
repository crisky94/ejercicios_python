# e. Verificar si una lista es un subconjunto de otra
# Dadas dos listas, verifica si todos los elementos de la primera lista están presentes en la segunda. Utiliza conjuntos para facilitar la verificación.

lista1 = [1, 2, 3]
lista2 = [1, 2, 3, 4, 5]
# Salida esperada: Lista1 es un subconjunto de Lista2.

es_subconjunto = set(lista1).issubset(set(lista2))

if es_subconjunto:
    print("Lista1 es un subconjunto de Lista2.")
else:
    print("Lista1 no es un subconjunto de Lista2.")
