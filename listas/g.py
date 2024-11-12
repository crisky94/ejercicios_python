# g. Filtrar números pares
# Dada una lista de números, crea una nueva lista solo con los números pares e imprémela.

numeros = [1, 2, 3, 4, 5, 6, 7, 8]
pares = []
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
print(pares)
# Debería imprimir: [2, 4, 6, 8]