def resta(a, b, c):
    return a - b - c

lista_numeros = [10, 3, 2]
#resta(lista[0], lista[1],lista[2]) = resta(*lista_numeros)
print(resta(*lista_numeros))