# a. Contando palabras
# Crea un diccionario que almacene el conteo de palabras en una oración dada. Pide al usuario que ingrese una oración y almacena en el diccionario cuántas veces aparece cada palabra.

texto = "hola mundo hola"

conteo_palabras = {}

for palabra in texto.split():
    if palabra not in conteo_palabras:
        conteo_palabras[palabra] = 1
    else:
        conteo_palabras[palabra] += 1
print(conteo_palabras)
# Salida esperada: {'hola', 2, 'mundo': 1}
