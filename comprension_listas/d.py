# d. Convertir a minúsculas
# Dada una lista de palabras con algunas en mayúsculas y otras en minúsculas, genera una nueva lista con todas las palabras en minúsculas.

palabras = ["PYTHON", "Listas", "Comprensión", "De", "Datos"]
minúsculas = []

for p in palabras:
    minúsculas.append(p.lower())
print(minúsculas)
# Salida esperada: ['python', 'listas', 'comprensión', 'de', 'datos']
