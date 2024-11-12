# a. Elevar al cuadrado
# Dada una lista de números, genera una nueva lista que contenga el cuadrado de cada número en la lista original.

numeros = [1, 2, 3, 4, 5]
numeros_cuadrados = []
for n in numeros:
    numeros_cuadrados.append(n**2) 
print(numeros_cuadrados)
# Salida esperada: [1, 4, 9, 16, 25]