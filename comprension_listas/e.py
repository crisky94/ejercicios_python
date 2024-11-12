# e. Obtener los primeros caracteres
# Dada una lista de palabras, genera una nueva lista que contenga solo el primer carácter de cada palabra.

palabras = ["python", "listas", "comprensión", "de", "datos"]
primer_caracter = []

for p in palabras:
    primer_caracter.append(p[0])
print(primer_caracter)
# Salida esperada: ['p', 'l', 'c', 'd', 'd']