# b. Encontrar elementos comunes entre dos listas
# Dadas dos listas, encuentra los elementos que están presentes en ambas y devuelve una lista con esos elementos únicos utilizando conjuntos.

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
listas = []

for l in lista1:
    for lista in lista2:
        if l == lista:
            listas.append(l)
print(listas)
    
# Salida esperada: [4, 5]