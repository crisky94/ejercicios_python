# e. Países y capitales
# Crea un diccionario con al menos cinco pares de países y sus respectivas capitales. Luego, permite al usuario ingresar el nombre de un país y muestra su capital. Si el país no está en el diccionario, muestra un mensaje de que no está registrado.

paises = {'Argentina': 'Buenos Aires', 'Brasil': 'Brasilia', 'Chile': 'Santiago'}

pais = 'Argentina'

if pais in paises:
    print(f"{pais}, Capital: {paises[pais]}")
else:
    print('No esta registrado.')
# Salida esperada: La capital de Chile es Santiago.