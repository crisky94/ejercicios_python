# a. Escribe una función es_anagrama que verifique si dos cadenas son anagramas (tienen las mismas letras en diferente orden). La función debe recibir los parámetros cadena1 y cadena2 y devolver True si ambas tienen los mismos caracteres.
anagramas = [
    ('Amor', 'Roma'),
    ('Nacionalista', 'Altisonancia'),
    ('Cobra', 'Barco'),
    ('Flamenco', 'Come flan'),
    ('Un legado', 'De alguno'),
]

def es_anagrama(cadena1, cadena2):
    return sorted(cadena1.lower()) == sorted(cadena2.lower())

for anagrama in anagramas:
    print(anagrama, es_anagrama(anagrama[0], anagrama[1]))
