# e. Ejercicio práctico
# Crea un diccionario que contenga información de un libro (título, autor, año, género). Modifica el género del libro y elimina el año de publicación.

libro = {
    "titulo": "Algun titulo",
    "autor": "Algun autor",
    "año": 1980,
    "género": "ciencia ficción"
}

libro["gênero"] = "acción"
print(libro)

libro.pop('año')