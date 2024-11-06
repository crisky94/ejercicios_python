# i. Identificación de elementos únicos
# Tienes una lista de números y quieres saber cuántas veces aparece cada número en la lista. Utiliza un diccionario para almacenar cada número y su conteo de apariciones, luego imprime el diccionario.

numeros = [1, 2, 2, 3, 3, 3, 4]
conteo = {}

for n in numeros:
    if n not in conteo:
        conteo[n] = 1
    else:
        conteo[n] += 1
print(conteo)
# Salida esperada: {1: 1, 2: 2, 3: 3, 4: 1}