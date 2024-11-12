# a. Eliminar duplicados de una lista
# Dada una lista con elementos duplicados, utiliza un conjunto para crear una nueva lista que contenga solo los elementos únicos.

nombres = ["Ana", "Luis", "Juan", "Ana", "Sofía", "Luis"]
print(f'{set(list(nombres))}')
# Salida esperada: ['Ana', 'Luis', 'Juan', 'Sofía']