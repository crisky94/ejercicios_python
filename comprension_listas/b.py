# b. Filtrar números pares
# Dada una lista de números, genera una nueva lista que contenga solo los números pares.

numeros = [10, 15, 20, 25, 30, 35, 40]
pares = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
print(pares)
# Salida esperada: [10, 20, 30, 40]