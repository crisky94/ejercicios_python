# d. Contar ocurrencias de un elemento
# Dada una lista de palabras, cuenta cuántas veces aparece una palabra específica en la lista e imprime el resultado.

palabras = ["hola", "mundo", "hola", "python", "hola"]
palabra_a_contar = "hola"
count = 0

for p in palabras:
    if p == palabra_a_contar:
        count += 1
print(f'La palabra "hola" aparece {count} veces')
# Debería imprimir: 3