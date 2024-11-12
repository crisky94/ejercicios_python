# c. Longitud de palabras
# Dada una lista de palabras, genera una nueva lista que contenga la longitud de cada palabra.

palabras = ["python", "comprensión", "de", "listas", "es", "útil"]
longitud  = []

for p in palabras:
    longitud.append(len(p))
print(longitud)
# Salida esperada: [6, 11, 2, 6, 2, 4]